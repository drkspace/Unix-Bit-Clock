import tkinter as tk
import time

class Clock(tk.Frame):

    def __init__(self, master = None, ):

        super().__init__(master)
        self.pack()
        self.create_widgets()

        self.update()

    def create_widgets(self):
        self.timeStampText = tk.StringVar()
        self.timeStamp = tk.Label(self.master, textvariable = self.timeStampText, font=("Courier", 25)).pack()

        self.currentTimeStampText = tk.StringVar()
        self.currentTimeStamp = tk.Label(self.master, textvariable = self.currentTimeStampText, font=("Courier", 25)).pack()
        
        #NUmber of bits in the Unix time stamp (need to change in 2038)
        self.bitsToUse = 64
        self.bits = []

        radius = 10
        self.canvas = tk.Canvas(self, width = self.bitsToUse*(radius+20), height = radius+50)
        self.canvas.pack()
        
        for i in range(self.bitsToUse):
            self.bits.append(self.canvas.create_oval(i*radius*2-radius+25, 25-radius, i*radius*2+radius+25, 25+radius, state = tk.DISABLED))

        #print(self.bits)


    def update(self):
        
        currentTime = int(time.time()*1000)
        #print(currentTime)
        self.timeStampText.set(str(currentTime/1000.0))
        self.currentTimeStampText.set(time.localtime())
        timeBits = list(str(format(currentTime, 'b')))
        while len(timeBits) < self.bitsToUse:
            timeBits = ['0'] + timeBits
        for i in range(self.bitsToUse):
            self.canvas.itemconfig(self.bits[i], fill = '#FFFFFF' if timeBits[i] == '0' else '#FF0000')
        #print(root.winfo_height())
        #print(root.winfo_width())
        self.after(1, self.update)

root = tk.Tk()
root.title("Unix Time Clock")
root.geometry("1303x136")
c = Clock(master=root)
c.mainloop()
c.update()

