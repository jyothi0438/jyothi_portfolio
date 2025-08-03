from tkinter import *
from time import strftime

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B/%d/%Y")
    date_label.config(text=date_string)

    day_label.after(1000, update)


window = Tk()
window.title("Digital Clock")

time_label = Label(window, font=("Arial", 50), fg="#EEEEEE", bg="black")
time_label.pack()

day_label = Label(window, font=("arial", 25))
day_label.pack()

date_label = Label(window, font=("Arial", 25))
date_label.pack()

update()
window.mainloop()