# GUI_Safe_Delete.py

import os
from tkinter import Tk, filedialog, messagebox, Button, Label
from send2trash import send2trash
from datetime import datetime

def log_deletion(file_path):
    with open('deletion_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()} - Deleted: {file_path}\n")

def select_and_delete():
    file_paths = filedialog.askopenfilenames(title="Delete karne ke liye files select karo")

    if not file_paths:
        messagebox.showinfo("No Selection", "Koi file select nahi ki gayi.")
        return

    for file_path in file_paths:
        confirm = messagebox.askyesno("Confirm Deletion", f"Kya aap '{os.path.basename(file_path)}' ko delete karna chahte ho?")
        if confirm:
            send2trash(file_path)
            log_deletion(file_path)
            messagebox.showinfo("Deleted", f"'{os.path.basename(file_path)}' Recycle Bin mein bhej diya gaya hai.")
        else:
            messagebox.showinfo("Cancelled", f"'{os.path.basename(file_path)}' delete cancel kar diya gaya hai.")

    messagebox.showinfo("Done", "Sabka process complete ho gaya. Log file mein details save ho gayi hain.")

# Main Window
root = Tk()
root.title("Safe File Deletion App")
root.geometry("400x200")

label = Label(root, text="Safe File Deletion Tool", font=("Arial", 16))
label.pack(pady=20)

delete_button = Button(root, text="Select Files to Delete", command=select_and_delete, font=("Arial", 12))
delete_button.pack(pady=10)

root.mainloop()