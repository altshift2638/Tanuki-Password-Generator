import random
import tkinter as tk
from tkinter import messagebox

def generate_passwords():
    try:
        number = int(entry_number.get())
        length = int(entry_length.get())
        
        chars = 'abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ!@#$%^&*()_1234567890\]}{p'
        passwords = []
        
        for pwd in range(number):
            password = ''.join(random.choice(chars) for _ in range(length))
            passwords.append(password)
        
        text_output.delete(1.0, tk.END)  # Clear any existing text
        for pwd in passwords:
            text_output.insert(tk.END, pwd + "\n")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for both fields.")

def restart():
    entry_number.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    text_output.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Tanuki Password Generator")
root.geometry("400x300")

# Create and place widgets
label_number = tk.Label(root, text="Amount of passwords:")
label_number.pack(pady=5)
entry_number = tk.Entry(root)
entry_number.pack(pady=5)

label_length = tk.Label(root, text="Password length:")
label_length.pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

btn_generate = tk.Button(root, text="Generate", command=generate_passwords)
btn_generate.pack(pady=10)

text_output = tk.Text(root, height=10, width=40)
text_output.pack(pady=5)

btn_restart = tk.Button(root, text="Restart", command=restart)
btn_restart.pack(pady=10)

# Start the GUI event loop
root.mainloop()
