from tkinter import Tk, Label


window = Tk()
window.title("Digital Clock")
window.geometry("600x300")

label = Label(window, font = ("Arial  ", 78, "bold"), bg= "steelblue", fg = 'white')
label.pack(pady =100)

from datetime import datetime
def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)

clock()
window.mainloop()
