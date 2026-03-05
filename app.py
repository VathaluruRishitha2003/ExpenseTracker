import pandas as pd
import matplotlib.pyplot as plt
import os

file_name = "expenses.csv"

if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["Category","Amount"])
    df.to_csv(file_name,index=False)

while True:
    print("\nExpense Tracker")
    print("1 Add Expense")
    print("2 Show Expenses")
    print("3 Total Spending")
    print("4 Show Graph")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        new_data = pd.DataFrame([[category,amount]],columns=["Category","Amount"])

        df = pd.read_csv(file_name)
        df = pd.concat([df,new_data],ignore_index=True)

        df.to_csv(file_name,index=False)

        print("Expense Saved!")

    elif choice == "2":
        df = pd.read_csv(file_name)
        print(df)

    elif choice == "3":
        df = pd.read_csv(file_name)
        print("Total Spending:",df["Amount"].sum())

    elif choice == "4":
        df = pd.read_csv(file_name)
        category_total = df.groupby("Category")["Amount"].sum()
        category_total.plot(kind="pie",autopct='%1.1f%%')
        plt.show()

    elif choice == "5":
        break