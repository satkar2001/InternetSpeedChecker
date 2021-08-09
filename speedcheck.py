from tkinter import *
from tkinter import messagebox
import pyspeedtest

def one():
    speed=pyspeedtest.SpeedTest("www.google.com")
    a1=(str(speed.download()))+"Bytes per second"
    messagebox.showinfo("your internet download speed",a1)

root=Tk()

root.title("speed checker")

root.config(bg='blue')

root.geometry("500x250")

label1=Label(root,text="speed checker",font=("Ariel",30,"bold"),bg="lightblue").pack()

button1=Button(root,text="check speed",font=("Ariel",20,"bold"),bg="yellow",height=1,width=10,command=one).pack()



root.mainloop()