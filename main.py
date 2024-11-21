import tkinter as tk
from tkinter import ttk

def handle_button_click(clicked_button_text):
    current_text = input_var.get()
    
    if clicked_button_text == "=":
        try:
            # Replace custom symbols with Python operators
            expression = current_text.replace("÷", "/").replace("x", "*")
            result = eval(expression)
            
            # Check if the result is a whole number
            if result.is_integer():
                result = int(result)
                
            input_var.set(result)
        except Exception:
            input_var.set("Error")
    elif clicked_button_text == "C":
        input_var.set("")
    elif clicked_button_text == "%":
        # Convert the current number to a percentage
        try:
            current_number = float(current_text)
            input_var.set(current_number / 100)
        except ValueError:
            input_var.set("Error")
    else:
        input_var.set(current_text + clicked_button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the result with larger font size
input_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=input_var, font=("Helvetica", 24), justify="right", state="readonly")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button layout
buttons = [
    ("C", 1, 0), ("+", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

# Configure style for theme
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Helvetica", 16), width=10, height=4)

# Create buttons and add them to the grid
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(
        root,
        text=button_text,
        command=lambda text=button_text: handle_button_click(text),
        style="TButton"
    )
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

# Configure row and column weights so they expand proportionally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Set the window size to a 9:16 ratio
width = 500
height = 700
root.geometry(f"{width}x{height}")

# Make the window non-resizable
root.resizable(False, False)

# Keyboard control
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<Key-BackSpace>", lambda event: handle_button_click("C"))

# Run the main loop
root.mainloop()
