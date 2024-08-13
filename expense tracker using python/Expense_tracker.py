from expense import Expense
import calendar
import datetime

def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 1000

    # Get user input for Expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and Summarize Expenses.
    summarize_expenses(expense_file_path, budget)

def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    # print(f"You've entered {expense_name}, for which you've paid {expense_amount} Rs.")

    expense_categories = [
        "🍜 Food", "🏚️ Home", "💼 Work", "🎳 Fun", "🔥 Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
            
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                new_expense = Expense(category=selected_category, name=expense_name, amount=expense_amount)
                return new_expense
            else:
                print("Invalid Category. Please try again!")

        except ValueError:
            print("Invalid input. Please enter a number corresponding to the category.")



def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense : {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding='utf-8') as f:
        f.write(f"{expense.category},{expense.name},{expense.amount}\n")

def summarize_expenses(expense_file_path, budget):
    print(f"🎯 Users Summarized Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_category, expense_name, expense_amount = stripped_line.split(",")
            line_expense = Expense(
                category = expense_category, name = expense_name, amount = float(expense_amount)
            )
            # print(line_expense)
            expenses.append(line_expense)
    # print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    # print(amount_by_category)
    print("Expenses By Category📈")
    for key, amount in amount_by_category.items():
        print(f" {key}: ₹{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent ₹{total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    # print(f"Budget Remaining ₹{remaining_budget:.2f} this month!")

    if remaining_budget < 0:
      print(f"Warning: Your budget is in the negative! You have overspent by ₹{-remaining_budget:.2f}.")
    elif remaining_budget < 1000:  # You can adjust the threshold as needed
     print(f"Alert: Your budget is getting low! Only ₹{remaining_budget:.2f} remaining this month.")
    else:
     print(f"Budget Remaining: ₹{remaining_budget:.2f} this month!")


    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    # print("Remaining days in the current month:", remaining_days)
    daily_budget = remaining_budget/remaining_days
    print(f"➡️ Budget Per Day: ₹{daily_budget:.2f}")


if __name__ == "__main__":
    main()
