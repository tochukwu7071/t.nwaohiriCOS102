import tkinter as tk
from tkinter import messagebox
import csv

# Function to load the employee data from the CSV file
def load_employee_data():
    employees = []
    with open('GIG-logistics.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees

# Load employee data
employee_data = load_employee_data()

# Set up the GUI window
root = tk.Tk()
root.title("GIG Logistics - Employee Verification")
root.geometry("400x300")

# Input fields
tk.Label(root, text="Enter Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Enter Department:").pack(pady=5)
dept_entry = tk.Entry(root)
dept_entry.pack(pady=5)

# Function to verify employee
def verify_employee():
    name = name_entry.get().strip()
    department = dept_entry.get().strip()

    # Check if the employee exists in the database
    employee_found = None
    department_members = []

    for employee in employee_data:
        if employee['Name'].lower() == name.lower() and employee['Department'].lower() == department.lower():
            employee_found = employee
        if employee['Department'].lower() == department.lower():
            department_members.append(employee['Name'])

    if employee_found:
        messagebox.showinfo("Welcome!", f"Welcome, {name}!\nHere are your team members:")

        # Show all department members
        members_list = "\n".join(department_members)
        messagebox.showinfo("Department Members", members_list)
    else:
        messagebox.showwarning("Not Found", "Sorry, you are not registered in the system.")

# Check button
tk.Button(root, text="Check", command=verify_employee).pack(pady=20)

root.mainloop()