'''
Task-01
Implement Caesar Cipher
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption.

'''

import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            shifted_char = chr((ord(char) - start + mode * shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

def encrypt_decrypt():
    message = entry_message.get()
    shift = int(entry_shift.get())

    if radio_var.get() == 1:  # Encryption
        result = caesar_cipher(message, shift, 1)
    else:  # Decryption
        result = caesar_cipher(message, shift, -1)

    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

def show_info():
    messagebox.showinfo("About", "Caesar Cipher GUI\n\nCreated by Usama Tayyab")

# Create main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create frames
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

frame_middle = tk.Frame(root)
frame_middle.pack(pady=5)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

# Widgets for top frame
label_message = tk.Label(frame_top, text="Message:")
label_message.grid(row=0, column=0, padx=5)

entry_message = tk.Entry(frame_top, width=50)
entry_message.grid(row=0, column=1, padx=5)

# Widgets for middle frame
label_shift = tk.Label(frame_middle, text="Shift:")
label_shift.grid(row=0, column=0, padx=5)

entry_shift = tk.Entry(frame_middle, width=10)
entry_shift.grid(row=0, column=1, padx=5)

radio_var = tk.IntVar()

radio_encrypt = tk.Radiobutton(frame_middle, text="Encrypt", variable=radio_var, value=1)
radio_encrypt.grid(row=0, column=2, padx=5)

radio_decrypt = tk.Radiobutton(frame_middle, text="Decrypt", variable=radio_var, value=2)
radio_decrypt.grid(row=0, column=3, padx=5)

# Widgets for bottom frame
button_process = tk.Button(frame_bottom, text="Encrypt/Decrypt", command=encrypt_decrypt)
button_process.pack(side=tk.LEFT, padx=5)

button_info = tk.Button(frame_bottom, text="About", command=show_info)
button_info.pack(side=tk.RIGHT, padx=5)

# Result entry
entry_result = tk.Entry(root, width=50)
entry_result.pack(pady=10)

# Start the GUI
root.mainloop()