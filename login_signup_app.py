from tkinter import *
from tkinter import messagebox
import os

# --------------------------
# FILE HANDLING – Store Users
# --------------------------
# We'll store user data in a simple text file: users.txt
# Each line format: username,password

USER_FILE = "users.txt"

# Ensure the file exists
if not os.path.exists(USER_FILE):
    open(USER_FILE, 'w').close()


# --------------------------
# LOGIN WINDOW
# --------------------------
def login_window():
    root = Tk()
    root.title("Login Page")
    root.geometry("350x250")
    root.resizable(False, False)

    Label(root, text="Login Page", font=("Arial", 16, "bold")).pack(pady=10)

    Label(root, text="Username").pack()
    username_entry = Entry(root)
    username_entry.pack()

    Label(root, text="Password").pack()
    password_entry = Entry(root, show="*")  # Mask password
    password_entry.pack()

    # --------------------------
    # LOGIN FUNCTION
    # --------------------------
    def login():
        uname = username_entry.get().strip()
        pwd = password_entry.get().strip()

        # Validation 1: Empty fields
        if not uname or not pwd:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Read stored users
        with open(USER_FILE, 'r') as f:
            users = [line.strip().split(',') for line in f if line.strip()]

        # Check credentials
        for user in users:
            if user[0] == uname and user[1] == pwd:
                messagebox.showinfo("Success", f"Welcome, {uname}!")
                root.destroy()
                return
        messagebox.showerror("Error", "Invalid Username or Password")

    # --------------------------
    # SWITCH TO SIGNUP PAGE
    # --------------------------
    def open_signup():
        root.destroy()
        signup_window()

    Button(root, text="Login", width=12, command=login).pack(pady=5)
    Button(root, text="Go to Signup", width=12, command=open_signup).pack()

    root.mainloop()


# --------------------------
# SIGNUP WINDOW
# --------------------------
def signup_window():
    win = Tk()
    win.title("Signup Page")
    win.geometry("350x300")
    win.resizable(False, False)

    Label(win, text="Signup Page", font=("Arial", 16, "bold")).pack(pady=10)

    Label(win, text="New Username").pack()
    new_user_entry = Entry(win)
    new_user_entry.pack()

    Label(win, text="New Password").pack()
    new_pass_entry = Entry(win, show="*")
    new_pass_entry.pack()

    Label(win, text="Confirm Password").pack()
    confirm_pass_entry = Entry(win, show="*")
    confirm_pass_entry.pack()

    # --------------------------
    # REGISTER FUNCTION
    # --------------------------
    def register():
        uname = new_user_entry.get().strip()
        pwd = new_pass_entry.get().strip()
        cpwd = confirm_pass_entry.get().strip()

        # Validation 1: Empty fields
        if not uname or not pwd or not cpwd:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Validation 2: Password match
        if pwd != cpwd:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Read existing users
        with open(USER_FILE, 'r') as f:
            users = [line.strip().split(',')[0] for line in f if line.strip()]

        # Validation 3: Username already exists
        if uname in users:
            messagebox.showerror("Error", "Username already exists!")
            return

        # Register user
        with open(USER_FILE, 'a') as f:
            f.write(f"{uname},{pwd}\n")

        messagebox.showinfo("Success", "Registration successful! Please login.")
        win.destroy()
        login_window()

    # --------------------------
    # CANCEL FUNCTION
    # --------------------------
    def cancel():
        win.destroy()
        login_window()

    Button(win, text="Register", width=12, command=register).pack(pady=5)
    Button(win, text="Cancel", width=12, command=cancel).pack()

    win.mainloop()


# --------------------------
# START THE PROGRAM
# --------------------------
login_window()
