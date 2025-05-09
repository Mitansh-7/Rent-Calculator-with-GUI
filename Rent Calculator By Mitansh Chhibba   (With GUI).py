#rent calculator in python

## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

## Output
# Total amount you've to pay is

import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        rent = int(entry_rent.get())
        food = int(entry_food.get())
        electricity_spend = int(entry_electricity.get())
        charge_per_unit = float(entry_charge.get())
        persons = int(entry_persons.get())

        total_bill = electricity_spend * charge_per_unit
        total_amount = food + rent + total_bill
        per_person = total_amount // persons

        result_label.config(text=f"Each person will pay = ₹ {per_person}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

# Create the GUI window
root = tk.Tk()
root.title("Rent Calculator By Mitansh Chhibba")
root.geometry("450x300")

# Input fields
tk.Label(root, text="Hostel/Flat Rent:").pack()
entry_rent = tk.Entry(root)
entry_rent.pack()

tk.Label(root, text="Total Food Ordered:").pack()
entry_food = tk.Entry(root)
entry_food.pack()

tk.Label(root, text="Electricity Units Spent:").pack()
entry_electricity = tk.Entry(root)
entry_electricity.pack()

tk.Label(root, text="Charge per Unit:").pack()
entry_charge = tk.Entry(root)
entry_charge.pack()

tk.Label(root, text="Number of Persons:").pack()
entry_persons = tk.Entry(root)
entry_persons.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack()

root.mainloop()
