import tkinter as tk

root = tk.Tk() #tkinter object initialized
root.title("Basic Calculator")
root.geometry("400x400")
root.resizable(False, False)

entry = tk.Entry(
    root, 
    font = ("Arial", 22),
    justify= "right",
    bd = 10
)

entry.pack(fill="both", padx=10, pady=10, ipady=10)

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)
    
def calculate():
    try:
        result = eval(entry.get())
        
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "cannot divide by zero")
    
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['3', '2', '1', '-'],
    ['0', '.', 'C', '+']
]

frame = tk.Frame(root)

frame.pack(expand=True, fill='both', padx=10, pady=5)

for row_index, row in enumerate(buttons):
    for col_index, value in enumerate(row):
        if value == 'C':
            command = clear
        
        else:
            command = lambda v=value: click(v)
        
        tk.Button(
            frame,
            text=value,
            font=('Arial', 18),
            command=command
        ).grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=3,
            pady=3,
            
        )
    

tk.Button(
    root,
    text='=',
    font=("Arial", 20),
    command=calculate,
    bg="lightblue",
    
).pack(
    fill="both", padx=10, pady=10
)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
    frame.grid_rowconfigure(i, weight=1)

root.mainloop()
        
    