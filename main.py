from tkinter import *
import tkinter as tk
import sys
import shutil, os, glob
from tkinter.filedialog import askdirectory
from tkinter import Tk, messagebox
import os , hashlib
from pathlib import Path

import tkinter.filedialog

import tkinter.messagebox




# Create the main window
root = tk.Tk()

root.geometry("480x320")
listbox = tk.Listbox(root)
label = tk.Label(root, text="Available drives:")
label2 = tk.Label(root, text="Deleted files:")
src_button = tk.Button(root, text='Select source directory', command=lambda: select_dir(src_entry))
src_button2 = tk.Button(root, text='Check from', command=lambda: select_dir(src_entry))

src_entry = tk.Entry(root)  
dest_button = tk.Button(root, text='Select destination directory', command=lambda: select_dir(dest_entry))
dest_button2 = tk.Button(root, text='DELETE from', command=lambda: select_dir(dest_entry))

dest_entry = tk.Entry(root)     
action = tk.StringVar(root)
copy_button = tk.Radiobutton(root, text='Copy', variable=action, value='Copy')
move_button = tk.Radiobutton(root, text='Move', variable=action, value='Move')
confirm_button = tk.Button(root, text='Confirm', command=lambda: copy_or_move_image_action(src_entry, dest_entry, action))
confirm_button2 = tk.Button(root, text='Confirm', command=lambda: find_duplicate_and_delete_action(src_entry, dest_entry))

def exit_application():
    # Close the main window and exit the application
    
    root.destroy()
    sys.exit()
button4 = tk.Button(root, background = "#61594D", text="Exit", command=exit_application, width=320)

     
        
        
# Create the buttons

# Define the callback functions for the buttons
def display_connected_drives():
    # Code to display connected drives goes here
    
    
    # List all the drives
    drives = os.listdir("/media/sami")
    
    # Hide the other buttons and label
   
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    
    # Create the main window
    
    root.title("Connected Drives")
    # Add a label to display the drives

    label.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    
    # Add a listbox to display the drives
    
    for drive in drives:
          listbox.delete(0, tk.END)
          listbox.insert(tk.END, drive)
    listbox.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    # Add a back button
    back_button.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1) 
    button4.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)


def show_main_page():
    src_button.pack_forget()
    src_button2.pack_forget()
    src_entry.pack_forget()
    dest_button.pack_forget()
    dest_button2.pack_forget()
    dest_entry.pack_forget()
    
    copy_button.pack_forget()
    move_button.pack_forget() 
    confirm_button.pack_forget()
    confirm_button2.pack_forget()
    listbox.pack_forget()
    label.pack_forget()
    label2.pack_forget()
    back_button.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    root.title("Camera Backup System")
    # Show the other buttons and label
    button1.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    button2.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    button3.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    button4.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
back_button = tk.Button(root, text="Back", command=show_main_page)
   


def copy_move_image():
    listbox.pack_forget()
    label.pack_forget()
    
    button4.pack_forget()
    
    button1.pack_forget()
    button3.pack_forget()

    root.title("Copy / Move Images")
    # Create a Button widget to open a directory selection dialog for the source directory
    src_button.pack()

    # Create an Entry widget to display the selected source directory
    
    src_entry.pack()

    # Create a Button widget to open a directory selection dialog for the destination directory
    dest_button.pack()

    # Create an Entry widget to display the selected destination directory
    
    dest_entry.pack()

    # Create a variable to store the selected action
    
    action.set('Copy')  # Set the default value to 'Copy'

    # Create a RadioButton widget to select 'Copy' action
    
    copy_button.pack()

    # Create a RadioButton widget to select 'Move' action
    
    move_button.pack()

    # Create a Button widget to confirm the directories and action
    
    confirm_button.pack()
    back_button.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1) 
    button4.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    # Run the Tkinter event loop
    root.mainloop()

def select_dir(entry):
    # Open a directory selection dialog and update the Entry widget with the selected directory
    dirname = tk.filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, dirname)
def copy_or_move_image_action(src_entry, dest_entry, action):
    # Get the selected directories from the Entry widgets
    src_dir = src_entry.get()
    dest_dir = dest_entry.get()
    listbox.delete(0, tk.END)
 
    # Perform the selected action (copy or move)
    if action.get() == 'Copy':
        print(f"Copied file: {src_dir}")
        listbox.insert(tk.END, f"Copied file: {src_dir}")
        shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
    else:
        # Check if both the are directories
        files = os.listdir(src_dir)
        for file in files:
            shutil.move(os.path.join(src_dir, file), dest_dir)
            print(f"Moved file: {file}")
            listbox.insert(tk.END, f"Moved file: {file}")
    
    listbox.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    tkinter.messagebox.showinfo("Success", "Task completed successfully")
def find_duplicate_and_delete():
   
    listbox.pack_forget()
    label.pack_forget()
    
    button4.pack_forget()
    button2.pack_forget()
    button1.pack_forget()
    
    root.title("Find & Delete Duplicate Files")
    # Create a Button widget to open a directory selection dialog for the source directory
    src_button2.pack()

    # Create an Entry widget to display the selected source directory
    
    src_entry.pack()

    # Create a Button widget to open a directory selection dialog for the destination directory
    dest_button2.pack()

    # Create an Entry widget to display the selected destination directory
    
    dest_entry.pack()

    # Create a variable to store the selected action
    

    # Create a Button widget to confirm the directories and action
    
    confirm_button2.pack()
    back_button.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1) 
    button4.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    # Run the Tkinter event loop
    root.mainloop()

def select_src_dir():
    # Open a directory selection dialog and set the selected directory as the value of the src_entry widget
    src_dir = filedialog.askdirectory()
    src_entry.delete(0, tk.END)
    src_entry.insert(0, src_dir)

def select_dest_dir():
    # Open a directory selection dialog and set the selected directory as the value of the dest_entry widget
    dest_dir = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_dir)

def find_duplicate_and_delete_action(src_entry, dest_entry):
    # Get the selected directories from the Entry widgets
    src_dir = src_entry.get()
    dest_dir = dest_entry.get()

    # Create a dictionary to store the hashes of unique files
    unique = dict()
    label2.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    # Calculate the hashes of the files in the first folder
    file_list = os.walk(src_dir)
    for root,folders,files in file_list:
        for file in files:
            path = Path(os.path.join(root,file))
            file_hash = hashlib.md5(open(path,'rb').read()).hexdigest()
            unique[file_hash] = path

    # Calculate the hashes of the files in the second folder
    file_list = os.walk(dest_dir)
    for root,folders,files in file_list:
        for file in files:
            path = Path(os.path.join(root,file))
            file_hash = hashlib.md5(open(path,'rb').read()).hexdigest()
            # Check if the file is a duplicate
            if file_hash in unique:
                # Duplicate file found, delete it
                os.remove(path)
                print(f"Deleted duplicate file: {path}")
                listbox.insert(tk.END, f"Deleted duplicate file: {path}")
                
                
            else:
                # Unique file, add it to the dictionary
                listbox.insert(tk.END, f"No Files Deleted")
                print(f"No Files Deleted")
                unique[file_hash] = path
            listbox.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
    tkinter.messagebox.showinfo("Success", "Task completed successfully")

root.title("Camera Backup System")

# Create the buttons
button1 = tk.Button(root, background = "#9AA4AD", text="Display Connected Drives", command=display_connected_drives, width=320 )
button2 = tk.Button(root, background = "#7893AD", text="Copy/Move Images", command=copy_move_image, width=320)

button3 = tk.Button(root, background = "#4D5761", text="Find Duplicate and Delete", command=find_duplicate_and_delete, width=320)

# Create a vertical layout to hold the buttons

button1.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
button2.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
button3.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)
button4.pack(side= TOP, expand = True, fill = BOTH, padx=2, pady=1)

# Display the main window
root.mainloop()
