from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Simple Calculator")

# Create the entry box
display = Entry(root, width=35, borderwidth=5, font=("Helvetica", 16))
display.grid(row=0, column=0, columnspan=5, padx=20, pady=20)

# Initialize variables
first_number = None
second_number = None
f_num = None
math_operation = None



# Button click functions
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, END)
    global first_number
    global second_number
    global math_operation
    global f_num
    first_number = None
    second_number = None
    math_operation = None
    f_num = None

def button_plus(arg=None):
    global first_number
    global math_operation
    global f_num
    math_operation = "addition"
    first_number = display.get()
    display.delete(0, END)
    f_num = float(first_number)
    

def button_minus(arg=None):
    global first_number
    global math_operation
    global f_num
    math_operation = "subtraction"
    first_number = display.get()
    display.delete(0, END)
    f_num = float(first_number)

def button_multiply(arg=None):
    global first_number
    global math_operation
    global f_num
    math_operation = "multiplication"
    first_number = display.get()
    display.delete(0, END)
    f_num = float(first_number)

def button_divide(arg=None):
    global first_number
    global math_operation
    global f_num
    math_operation = "division"
    first_number = display.get()
    display.delete(0, END)
    f_num = float(first_number)

def button_equal(arg=None):
    global second_number
    global math_operation
    global f_num
    if f_num is not None:
        second_number = display.get()
        display.delete(0, END)

        if math_operation == "addition":
            result = f_num + float(second_number)
            display.insert(0, result)
            log_entry = f"{f_num} + {second_number} = {result}\n"
        elif math_operation == "subtraction":
            result = f_num - float(second_number)
            display.insert(0, result)
            log_entry = f"{f_num} - {second_number} = {result}\n"
        elif math_operation == "multiplication":
            result = f_num * float(second_number)
            display.insert(0, result)
            log_entry = f"{f_num} * {second_number} = {result}\n"
        elif math_operation == "division":
            result = f_num / float(second_number)
            display.insert(0, result)
            log_entry = f"{f_num} / {second_number} = {result}\n"
        f_num = None
        log = ""
        log += log_entry

        # Save the log to a file
        with open("calculator.log", "a") as f:
            f.write(log_entry)
import os
import sys


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)



def open_log(arg=None):
    log_file = "calculator.log"
    file_path = os.path.join(os.getcwd(), log_file)
    with open(file_path, "r") as f:
        log_contents = f.read()

    log_window = Toplevel(root)
    log_window.title("calculator")
    log_text = Text(log_window)
    log_text.insert(END, log_contents)
    log_text.pack()



# Bind the keyboard keys
root.bind('<Return>', button_equal) # 'Return' key for equal
root.bind('<KP_Enter>', button_equal) # 'Enter' key on numpad for equal
root.bind('<plus>', button_plus) # '+' key for addition
root.bind('<minus>', button_minus) # '-' key for subtraction
root.bind('<asterisk>', button_multiply) # '*' key for multiplication
root.bind('<slash>', button_divide) # '/' key for division
root.bind('<BackSpace>', lambda event: display.delete(len(display.get())-1, END)) # 'Backspace' key for deleting the last digit
root.bind("<r>", lambda event: restart_program())
root.bind("<`>", open_log)

# Bind the number keys
for i in range(10):
    root.bind(str(i), lambda event, i=i: button_click(i))

# Define the buttons
restart_button = Button(root, text="Restart (r)", command=restart_program)
button_1 = Button(root, text="1", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, font=("Helvetica", 16), command=button_plus)
button_equal = Button(root, text="=", padx=40, pady=20, font=("Helvetica", 16), command=button_equal)
button_clear = Button(root, text="C", padx=38, pady=20, font=("Helvetica", 16), command=button_clear)
button_subtract = Button(root, text="-", padx=42, pady=20, font=("Helvetica", 16), command=button_minus)
button_multiply = Button(root, text="*", padx=42, pady=20, font=("Helvetica", 16), command=button_multiply)
button_divide = Button(root, text="/", padx=43, pady=20, font=("Helvetica", 16), command=button_divide)
button_log = Button(root, text="Log", padx=37, pady=20, command=open_log)


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_clear.grid(row=4, column=0)
button_add.grid(row=1, column=4)
button_equal.grid(row=4, column=2)

button_subtract.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)
root.configure(background="#333333")

root.mainloop()

