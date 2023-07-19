#GUI Tkinter Calculator in Python

from tkinter import *

equation = ''
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ''
    label_result.config(text=equation)

def calculate():
    global equation
    result = ''
    if equation !='':
        try:
            result = eval(equation)
        except:
            result ='ERROR'
            equation = ''
    label_result.config(text=result)
    

root = Tk()
root.title('Calculator')
root.geometry('570x600')
root.resizable(False, False)
root.configure(bg='gray14')



label_result = Label(root, width=25, height=2, text='', font=('Roboto',30))
label_result.pack()

erase = Button(root, width='5', height=1, activebackground='red4', bg='SpringGreen4', fg='gray1', text='C', font=('Roboto',30, "bold"), command=lambda: clear()).place(x=10, y=100)
divison = Button(root, width='5', height=1, activebackground='red4', bg='gray23', fg='gray1', text='/', font=('Roboto',30, "bold"), command=lambda: show('/')).place(x=150, y=100)
percentedge = Button(root, width='5', height=1, activebackground='red4', bg='gray23', fg='gray1', text='%', font=('Roboto',30, "bold"), command=lambda: show('%')).place(x=290, y=100)
multiplication = Button(root, width='5', height=1, activebackground='red4', bg='gray23', fg='gray1', text='x', font=('Roboto',30, "bold"), command=lambda: show('*')).place(x=430, y=100)

seven = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='7', font=('Roboto',30, "bold"), command=lambda: show('7')).place(x=10, y=200)
eight = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='8', font=('Roboto',30, "bold"), command=lambda: show('8')).place(x=150, y=200)
nine = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='9', font=('Roboto',30, "bold"), command=lambda: show('9')).place(x=290, y=200)
substraction = Button(root, width='5', height=1, activebackground='red4', bg='gray23', fg='gray1', text='-', font=('Roboto',30, "bold"), command=lambda: show('-')).place(x=430, y=200)

four = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='4', font=('Roboto',30, "bold"), command=lambda: show('4')).place(x=10, y=300)
five = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='5', font=('Roboto',30, "bold"), command=lambda: show('5')).place(x=150, y=300)
six = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='6', font=('Roboto',30, "bold"), command=lambda: show('6')).place(x=290, y=300)
addition = Button(root, width='5', height=1, activebackground='red4', bg='gray23', fg='gray1', text='+', font=('Roboto',30, "bold"), command=lambda: show('+')).place(x=430, y=300)

one = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='1', font=('Roboto',30, "bold"), command=lambda: show('1')).place(x=10, y=400)
two = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='2', font=('Roboto',30, "bold"), command=lambda: show('2')).place(x=150, y=400)
three = Button(root, width='5', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='3', font=('Roboto',30, "bold"), command=lambda: show('3')).place(x=290, y=400)
zero = Button(root, width='11', height=1, activebackground='cyan3', bg='SeaGreen3', fg='gray1', text='0', font=('Roboto',30, "bold"), command=lambda: show('0')).place(x=10, y=500)

comma = Button(root, width='5', height=1, activebackground='red4', bg='gray23', fg='gray1', text='.', font=('Roboto',30, "bold"), command=lambda: show('.')).place(x=290, y=500)
equal = Button(root, width='5', height=3, activebackground='red4', bg='tan1', fg='gray1', text='=', font=('Roboto',30, "bold"), command=lambda: calculate()).place(x=430, y=400)



root.mainloop()
