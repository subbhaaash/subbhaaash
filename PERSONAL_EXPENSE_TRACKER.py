#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Global list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount! Try again.")
        return
    description = input("Enter description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("✅ Expense added successfully!")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("📭 No expenses recorded.")
        return

    print("\n🧾 Your Expenses:")
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['description']}")


# In[17]:


add_expense()
view_expenses()


# In[11]:


# Global variable for monthly budget
monthly_budget = 0.0

# Set the monthly budget
def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print(f"✅ Monthly budget of ₹{monthly_budget} set successfully.")
    except ValueError:
        print("❌ Invalid budget input!")

# Track current spending vs budget
def track_budget():
    total = sum(e['amount'] for e in expenses)
    print(f"\n💰 Total Expenses: ₹{total}")
    print(f"📊 Monthly Budget: ₹{monthly_budget}")

    if total > monthly_budget:
        print("⚠️ You have exceeded your budget!")
    else:
        remaining = monthly_budget - total
        print(f"✅ You have ₹{remaining:.2f} left for the month.")


# In[19]:


set_budget()
track_budget()


# In[21]:


import csv

def load_expenses(filename="expenses.csv"):
    global expenses
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = []  # Reset current list
            for row in reader:
                # Convert amount from string to float
                row['amount'] = float(row['amount'])
                expenses.append(row)
        print("✅ Expenses loaded successfully from file.")
    except FileNotFoundError:
        print("⚠️ No existing file found. Starting fresh.")


# In[23]:


def save_expenses(filename="expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print("✅ Expenses saved successfully to file.")


# In[25]:


load_expenses()
save_expenses()


# In[ ]:




