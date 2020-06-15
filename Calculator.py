# This will be the start of a quick gui powered calculator that will allow me to catch up a bit on my python skills

from tkinter import *
from tkinter import messagebox


# def clear_all():
#    """This function will delete all entries from the calculator"""
#    return


def addition():
    """This function will be responsible for the addition functions in the graphic calculator"""
    error_handler()
    f1.delete(0, END)
    a1 = float(operand.get())
    a2 = float(operator.get())
    result = a1 + a2
    f1.insert(10, str(result))


def subtraction():
    """This function will be responsible for the subtraction functions in the graphic calculator"""
    error_handler()
    f1.delete(0, END)
    s1 = float(operand.get())
    s2 = float(operator.get())
    result = s1 - s2
    f1.insert(10, str(result))


def multiplication():
    """This function will be responsible for the subtraction functions in the graphic calculator"""
    error_handler()
    f1.delete(0, END)
    m1 = float(operand.get())
    m2 = float(operator.get())
    result = m1 * m2
    f1.insert(10, str(result))


def division():
    """This function will be responsible for the subtraction functions in the graphic calculator"""
    error_handler()
    f1.delete(0, END)
    d1 = float(operand.get())
    d2 = float(operator.get())
    result = d1 / d2
    f1.insert(10, str(result))


def error_handler():
    try:
        float(operand.get())
    except ValueError:
        messagebox.showerror(title="Input Error", message="Please Input a Number (e.g. 1,2,3)")
    except ZeroDivisionError:
        messagebox.showerror(title="Input Error", message="Dividing by zero")


# Driver Code
if __name__ == "__main__":
    master = Tk()
    master.title("Simple Calculator")
    master.geometry("525x260")
    Label(master, text='Operand').grid(row=0)
    Label(master, text='Operator').grid(row=1)
    Label(master, text='Result').grid(row=4)
    operand = Entry(master)
    operator = Entry(master)
    operand.grid(row=0, column=1)
    operator.grid(row=1, column=1)
    f1 = Entry(master)
    f1.grid(row=4, column=1)
    add_button = Button(master, text="+", command=addition).grid(row=2, column=2)
    sub_button = Button(master, text="-", command=subtraction).grid(row=2, column=3)
    mult_button = Button(master, text="*", command=multiplication).grid(row=3, column=2)
    div_button = Button(master, text="/", command=division).grid(row=3, column=3)
    mainloop()
