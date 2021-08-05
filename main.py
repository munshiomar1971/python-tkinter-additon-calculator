# simple calculator by omar sumon
#imports libraries and frameworks
from tkinter import *
# delcare the root

root = Tk()
root.title("Addition Calculator")

# declares e

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# button click function (adds number when button is clicked on)

def buttond_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number)) 

# button clear funtion (clears all the numbers when clicked on)

def buttond_clear():
	e.delete(0, END)

# button add function (adds numbers together when clicked)

def buttond_add():
	first_num = e.get()	
	global f_num 
	f_num = int(first_num)
	e.delete(0, END)

# button equal function (shows the result of the added numbers when clicked)
def buttond_eq():
	second_num = e.get()
	e.delete(0, END)
	e.insert(0, f_num + int(second_num))


# buttons

btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttond_click(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttond_click(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttond_click(3))

btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttond_click(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttond_click(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttond_click(6))

btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttond_click(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttond_click(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttond_click(9))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttond_click(0))

btn_add = Button(root, text="+", padx=39, pady=20, command=buttond_add)
btn_eq = Button(root, text="=", padx=91, pady=20, command=lambda: buttond_eq())
btn_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: buttond_clear())

# display buttons

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

btn_add.grid(row=5, column=0)
btn_eq.grid(row=5, column=1, columnspan=2)
btn_clear.grid(row=4, column=1, columnspan=2)


root.mainloop()