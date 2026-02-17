import tkinter as tk

root = tk.Tk()
root.title("Interactive Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#1e3c72")

display = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify='right')
display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

def append(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        if not expression:
            return
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

frame = tk.Frame(root, bg="#1e3c72")
frame.pack(expand=True, fill='both')

buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','C','+'),
]

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e3c72")
    row_frame.pack(expand=True, fill='both')
    for btn in row:
        if btn == 'C':
            action = clear_display
        else:
            action = lambda x=btn: append(x)
        tk.Button(row_frame, text=btn, font=("Arial",14), command=action).pack(side='left', expand=True, fill='both', padx=2, pady=2)

tk.Button(root, text="=", font=("Arial",16), bg="green", fg="white", command=calculate).pack(fill='both', padx=10, pady=5, ipady=10)

def key_input(event):
    key = event.char
    if key and key in '0123456789+-*/.':
        append(key)
    elif event.keysym == 'Return':
        calculate()
    elif event.keysym == 'BackSpace':
        current = display.get()
        if len(current) > 0:
            display.delete(len(current)-1, tk.END)
    elif event.keysym == 'Escape':
        clear_display()

root.bind("<Key>", key_input)

root.mainloop()
