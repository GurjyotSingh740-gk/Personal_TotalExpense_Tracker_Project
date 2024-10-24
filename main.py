import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Functions
def calculate_monthly_salary(annual_salary):
    return round(annual_salary / 12, 2)

def calculate_savings(monthly_salary, monthly_expenses):
    return round(monthly_salary - monthly_expenses, 2)

def store_monthly_expense(month, expense, expense_dict):
    expense_dict[month] = expense

def create_line_graph(expense_dict):
    months = list(expense_dict.keys())
    expenses = list(expense_dict.values())
    
    plt.figure(figsize=(8, 5))
    plt.plot(months, expenses, marker='o', color='blue', linestyle='-', label='Expenses')
    
    plt.title('Monthly Expenses Over Time')
    plt.xlabel('Month')
    plt.ylabel('Expense (₹)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Main window setup
root = tk.Tk()
root.title("Salary and Expense Tracker")
root.geometry("600x600")

# Labels
tk.Label(root, text="Enter Annual Salary (₹):").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Enter Monthly Expenses (₹):").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Select Month:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="Monthly Salary (₹):").grid(row=3, column=0, padx=10, pady=10)
tk.Label(root, text="Total Savings (₹):").grid(row=4, column=0, padx=10, pady=10)

# Entry boxes
annual_salary = tk.Entry(root)
monthly_expenses = tk.Entry(root)
month_entry = tk.Entry(root)
monthly_salary_label = tk.Label(root, text="")
savings_label = tk.Label(root, text="")

# Placing entry boxes and labels
annual_salary.grid(row=0, column=1)
monthly_expenses.grid(row=1, column=1)
month_entry.grid(row=2, column=1)
monthly_salary_label.grid(row=3, column=1)
savings_label.grid(row=4, column=1)

# Checkbox for graph display
show_line_graph = tk.BooleanVar()
graph_check = tk.Checkbutton(root, text="Show Monthly Expense Line Graph", variable=show_line_graph)
graph_check.grid(row=5, column=1, padx=10, pady=10)

# Initialize storage for expenses
monthly_expenses_dict = {}

def calculate_and_store():
    try:
        annual_salary_value = float(annual_salary.get())
        monthly_expenses_value = float(monthly_expenses.get())
        month = month_entry.get().strip().capitalize()
        
        if not month:
            raise ValueError("Month cannot be empty")
        
        monthly_salary = calculate_monthly_salary(annual_salary_value)
        monthly_salary_label.config(text=f"₹ {monthly_salary}")
        
        savings = calculate_savings(monthly_salary, monthly_expenses_value)
        savings_label.config(text=f"₹ {savings}")
        
        store_monthly_expense(month, monthly_expenses_value, monthly_expenses_dict)
        
        if show_line_graph.get():
            create_line_graph(monthly_expenses_dict)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers and month.")

# Buttons
calculate_btn = tk.Button(root, text="Calculate & Store", command=calculate_and_store)
calculate_btn.grid(row=6, column=0, padx=10, pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
