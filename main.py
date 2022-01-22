import pyperclip as clp
from tkinter import *
from datetime import date

url = ""


def on_focus_out(event):
    T1.selection_range(0, END)


def on_focus_in(event):
    global url
    url = clp.paste().strip()


def book():
    pass


def web():
    text = f"{T1.get()} [online]. [cit.{date.today()}]. Dostupné z: {url}"
    label.config(text=text)
    clp.copy(text)


def on_key_press(event):
    web()


root = Tk()
root.title("Citace")
root.geometry("320x90-50+50")
root.attributes("-alpha", 0.8)
command = IntVar()
root.grid()


T1 = Entry(root)
T1.grid(sticky="w", column=0, row=0)


R1 = Radiobutton(root, text="Web", variable=command, value=1, command=web)
R1.grid(sticky="w", column=0, row=1)
R1.select()

R2 = Radiobutton(root, text="Kniha", variable=command, value=2, command=book, state="disable")
R2.grid(sticky="w", column=0, row=2)

label = Label(root)
label.grid(sticky="w", column=0, row=3)


root.bind("<FocusIn>", on_focus_in)
root.bind("<FocusOut>", on_focus_out)
root.bind("<KeyPress>", on_key_press)

root.attributes('-topmost', True)

root.mainloop()
