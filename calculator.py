import tkinter as tk
from tkinter import messagebox as mb


L = []
a = "+"
S = ""

# ------------------------------------------------------- Retrieving the value of the button and displaying the same -------------------------------------------------------

def ret_and_dis(n1 = 0):
    
    global L
    global a
    global S
        
    if n1 != "$":
        
        if (a == "+" or a == "-" or a == "*" or a == "/" or a == "%") and (n1 == "+" or n1 == "-" or n1 == "*" or n1 == "/" or n1 == "%"):
            mb.showerror("Error", "Invalid")
            
        else:
            L.append(n1)
            S = S + str(n1)
            
        a = n1
        
        # print(L)
        # print(S)
        
        Result.place(x = 0, y = 0)
        Result.config( text = S, width = 50, height = 6, bg = "white", bd = 5, justify = "right")
        
# -------------------------------------------------------------- Clear function when C button is clicked ------------------------------------------------------------------
        
def clear():
    
    global L
    global S
    
    L = []
    S = ""
    
    Result.place(x = 0, y = 0)
    Result.config( text = 0, width = 50, height = 6, bg = "white", bd = 5, justify = "right")

# ------------------------------------------------------------------- Calculation of the final result --------------------------------------------------------------------    

def equals():
    
    global L
    global S
    x = []
    a = "0"

    # ------------------------------------------------------- Appending of numbers ------------------------------------------------------
    
    for i in L:
        if not (i == "+" or i == "-" or i == "*" or i == "/" or i == "%"):
            a = a + str(i)                                                  
            
        if (i == "+" or i == "-" or i == "*" or i == "/" or i == "%"):
            x.append(int(a))
            x.append(i)
            a = ""
        
    if i == L[len(L) - 1]:
        if a != "":
            x.append(int(a))
        else:
            x.append(a)

    # ----------------------------------------------------- Check of invalid expression ---------------------------------------------------
    
    if(x[len(x) - 1] == "+" or x[len(x) - 1] == "-" or x[len(x) - 1] == "*" or x[len(x) - 1] == "/" or x[len(x) - 1] == "%" or x[len(x) - 1] == ""):
        mb.showerror("Error", "Invalid expression")
        S = ""
        L = []
        
    # ---------------------------------------------------------- Actual Calculation --------------------------------------------------------
    
    i = 1
    j = 0
    a = 0
    op = ""
    b = 0
    result = [x[0]]
    
    while i in range(len(x)):
        
        a = int(result[j])
        if (x[i] == "+" or x[i] == "-" or x[i] == "*" or x[i] == "/" or x[i] == "%"):
            op = x[i]
        else:
            a = x[i]
        b = int(x[i + 1])
        
        if op == "+":
            result.append((a + b))
        elif op == "-":
            result.append((a - b))
        elif op == "*":
            result.append((a * b))
        elif op == "/":
            result.append((a / b))
        elif op == "%":
            result.append((a % b))
            
        i = i + 2
        j = j + 1
        
        # print(result)
        
        res = result[len(result) - 1]
        
        Result.place(x = 0, y = 0)
        Result.config( text = res, width = 50, height = 6, bg = "white", bd = 5, justify = "right")
        
# --------------------------------------------------------------------------------- GUI -----------------------------------------------------------------------------------
        
GUI = tk.Tk()
GUI.resizable( 0, 0 )
GUI.geometry( "350x350" )
GUI.title("CALCULATOR FOR FUN")

# ------------------------------------------------------ Result Box --------------------------------------------------------------

Result = tk.Label(GUI, text = "0")
Result.place(x = 10, y = 40)
Result.config( text = S, width = 50, height = 6, bg = "white", bd = 5)

# ----------------------------------------------- Number and symbol buttons ------------------------------------------------------

# -------------------------------------------------------- Numbers ---------------------------------------------------------------

one = tk.Button(GUI, text = "1", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(1))
one.place(x = 10, y = 110) 
one.config(height = 3, width = 10)

four = tk.Button(GUI, text = "4", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(4))
four.place(x = 10, y = 170)
four.config(height = 3, width = 10)

seven = tk.Button(GUI, text = "7", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(7))
seven.place(x = 10, y = 230)
seven.config(height = 3, width = 10)

two = tk.Button(GUI, text = "2", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(2))
two.place(x = 95, y = 110)
two.config(height = 3, width = 10)

five = tk.Button(GUI, text = "5", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(5))
five.place(x = 95, y = 170)
five.config(height = 3, width = 10)

eight = tk.Button(GUI, text = "8", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(8))
eight.place(x = 95, y = 230)
eight.config(height = 3, width = 10)

three = tk.Button(GUI, text = "3", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(3))
three.place(x = 180, y = 110)
three.config(height = 3, width = 10)

six = tk.Button(GUI, text = "6", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(6))
six.place(x = 180, y = 170)
six.config(height = 3, width = 10)

nine = tk.Button(GUI, text = "9", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(9))
nine.place(x = 180, y = 230)
nine.config(height = 3, width = 10)

zero = tk.Button(GUI, text = "0", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis(0))
zero.place(x = 95, y = 290)
zero.config(height = 3, width = 10)

# --------------------------------------------------------- Symbols --------------------------------------------------------------

plus = tk.Button(GUI, text = "+", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis("+"))
plus.place(x = 265, y = 110)
plus.config(height = 3, width = 10)

minus = tk.Button(GUI, text = "-", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis("-"))
minus.place(x = 265, y = 170)
minus.config(height = 3, width = 10)

prod = tk.Button(GUI, text = "*", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis("*"))
prod.place(x = 265, y = 230)
prod.config(height = 3, width = 10)

equals = tk.Button(GUI, text = "=", activebackground = "grey", activeforeground = "black", command = equals)
equals.place(x = 180, y = 290)
equals.config(height = 3, width = 10)

div = tk.Button(GUI, text = "/", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis("/"))
div.place(x = 265, y = 290)
div.config(height = 3, width = 4)

mod = tk.Button(GUI, text = "%", activebackground = "grey", activeforeground = "black", command = lambda : ret_and_dis("%"))
mod.place(x = 305, y = 290)
mod.config(height = 3, width = 4)

c = tk.Button(GUI, text = "c", activebackground = "grey", activeforeground = "black", command = clear)
c.place(x = 10, y = 290)
c.config(height = 3, width = 10)


Result.pack(side = "top")
GUI.mainloop()


