import datetime
import os
import pandas as pd


# Function to save data into Excel sheet
def save_to_excel(transaction_type, amount, current_balance):
  file_name = "atm_transactions.xlsx"
  now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  new_data = pd.DataFrame([{
      "Date & Time": now,
      "Transaction Type": transaction_type,
      "Amount": amount,
      "Balance Left": current_balance,
  }])

  # Check if the Excel file already exists
  if os.path.exists(file_name):
    df = pd.read_excel(file_name)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(file_name, index=False)
  else:
    new_data.to_excel(file_name, index=False)


# Initial Account Balance & PIN
balance = 10000
correct_pin = 1234

print("=== Welcome to Python ATM System ===")

# PIN Verification
entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == correct_pin:
  print("\nLogin Successful!\n")

  while True:
    print("--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
      print(f"\nYour current balance is: ₹{balance}\n")

    elif choice == "2":
      amount = float(input("Enter amount to deposit: "))
      if amount > 0:
        balance += amount
        print(f"₹{amount} deposited successfully!")
        print(f"Updated Balance: ₹{balance}\n")
        save_to_excel("Deposit", amount, balance)
      else:
        print("Invalid amount!\n")

    elif choice == "3":
      amount = float(input("Enter amount to withdraw: "))
      if 0 < amount <= balance:
        balance -= amount
        print(f"Please collect your cash: ₹{amount}")
        print(f"Remaining Balance: ₹{balance}\n")
        save_to_excel("Withdraw", amount, balance)
      elif amount > balance:
        print("Insufficient balance!\n")
      else:
        print("Invalid amount!\n")

    elif choice == "4":
      print("Thank you for using Python ATM. Have a great day!")
      break
    else:
      print("Invalid choice! Please select between 1 to 4.\n")

else:
  print("Incorrect PIN! Access Denied.")
  