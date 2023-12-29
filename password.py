import random
import string
import tkinter as tk
from tkinter import Label, Button, Entry, StringVar, Checkbutton

def generate_password():
    length = int(length_var.get())
    complexity = complexity_var.get()

    characters = string.ascii_letters

    if complexity == "medium":
        characters += string.digits
    elif complexity == "high":
        characters += string.digits + "@#&*"

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and pack widgets
Label(app, text="Enter Password Length:").grid(row=0, column=0, pady=5)
length_var = StringVar()
length_entry = Entry(app, textvariable=length_var)
length_entry.grid(row=0, column=1, pady=5)

Label(app, text="Enter Difficulty Level:").grid(row=1, column=0, pady=5)
complexity_var = StringVar()

low_button = Checkbutton(app, text="Low", variable=complexity_var, onvalue="low", offvalue="", bg="light blue")
low_button.grid(row=1, column=1, padx=5)

medium_button = Checkbutton(app, text="Medium", variable=complexity_var, onvalue="medium", offvalue="", bg="light blue")
medium_button.grid(row=1, column=2, padx=5)

high_button = Checkbutton(app, text="High", variable=complexity_var, onvalue="high", offvalue="", bg="light blue")
high_button.grid(row=1, column=3, padx=5)

generate_button = Button(app, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=4, pady=10)

Label(app, text="Generated Password:").grid(row=3, column=0, columnspan=4, pady=5)
password_var = StringVar()
generated_password_label = Label(app, textvariable=password_var, font=("Helvetica", 12), wraplength=300)
generated_password_label.grid(row=4, column=0, columnspan=4, pady=10)

# Start the application
app.mainloop()













