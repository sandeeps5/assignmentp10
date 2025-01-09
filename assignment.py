import tkinter as tk
from tkinter import messagebox

# Function to add key-value pair to the dictionary
def add_key():
    try:
        # Get key and value from the user input
        key = int(entry_key.get())  # Convert the key to an integer
        value = int(entry_value.get())  # Convert the value to an integer
        
        # Add to the dictionary
        sample_dict[key] = value
        
        # Show success message
        messagebox.showinfo("Success", f"Key {key} with value {value} added to dictionary!")
        
        # Update the dictionary display
        label_dict.config(text=f"Updated Dictionary: {sample_dict}")
        
    except ValueError:
        # If user inputs a non-integer value, show error
        messagebox.showerror("Invalid input", "Please enter valid integers for key and value.")

# Initialize the sample dictionary
sample_dict = {0: 10, 1: 20}

# Create the main window
root = tk.Tk()
root.title("Add Key to Dictionary")

# Create and place the dictionary display label
label_dict = tk.Label(root, text=f"Current Dictionary: {sample_dict}")
label_dict.pack(pady=10)

# Create and place the Key entry label and input box
label_key = tk.Label(root, text="Enter Key:")
label_key.pack()
entry_key = tk.Entry(root)
entry_key.pack(pady=5)

# Create and place the Value entry label and input box
label_value = tk.Label(root, text="Enter Value:")
label_value.pack()
entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# Create and place the Add Key button
button_add = tk.Button(root, text="Add Key", command=add_key)
button_add.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
