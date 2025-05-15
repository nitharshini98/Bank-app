import os
import random  

# -------------------- Account Creation -------------------------- #
Account = {}

def get_customer_info():
    Name = input("Enter your name: ")
    Address = input("Enter your address: ")
    NIC = input("Enter your NIC number: ")
    user_name = input("Enter your user name: ")
    password = input("Enter your PIN number: ")
    Phone_number = int(input("Enter your phone number: "))
    Initial_balance = float(input("Enter your initial balance: "))

    return Name, Address, NIC, user_name, password, Phone_number, Initial_balance

def Generated_Account_Number():
    global Account
    while True:
        Account_Number = random.randint(10000, 11000)
        if Account_Number not in Account:
            return Account_Number

def Create_customer():
    customer = get_customer_info()
    Account_number = Generated_Account_Number()

    Account[Account_number] = {
        "name": customer[0],
        "password": customer[4],
        "address": customer[1],
        "NIC": customer[2],
        "phone_number": customer[5],
        "Initial_balance": customer[6],
        "Transaction_History": []
    }
    print(f"Account created successfully! Your account number is: {Account_number}")

    # Saving to files
    with open('customer.txt', 'a') as customer_file, open('user.txt', 'a') as user_file:
        customer_file.write(f"{Account_number},{customer[0]},{customer[1]},{customer[2]},{customer[5]},{customer[6]}\n")
        user_file.write(f"{customer[3]},{customer[4]}\n")
    
    print("Account details saved.")

# ------------------------ Deposit Money ------------------------ #
def Deposit_money():
    global Account_Number
    Account_Number = int(input("Enter your Account Number: "))
    if Account_Number in Account:
        try:
            Deposit = float(input("Enter amount to deposit: $"))
            if Deposit > 0:
                Account[Account_Number]["Initial_balance"] += Deposit
                Account[Account_Number]["Transaction_History"].append(f"Deposited ${Deposit:.2f}")
                print(f"Deposit successful! Your new balance is: ${Account[Account_Number]['Initial_balance']:.2f}")
                save_transaction(Account_Number)
            else:
                print("Deposit amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid amount.")
    else:
        print("Account number not found.")

# ------------------------ Withdraw Money ----------------------- #
def Withdraw_money():
    global Account_Number
    Account_Number = int(input("Enter your Account Number: "))
    if Account_Number in Account:
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount > Account[Account_Number]["Initial_balance"]:
                print("Insufficient funds.")
            else:
                Account[Account_Number]["Initial_balance"] -= amount
                Account[Account_Number]["Transaction_History"].append(f"Withdrew ${amount:.2f}")
                print(f"Withdrawal successful! Your new balance is: ${Account[Account_Number]['Initial_balance']:.2f}")
                save_transaction(Account_Number)
        except ValueError:
            print("Please enter a valid amount.")
    else:
        print("Account number not found.")

# ------------------------ Check Balance ------------------------ #
def Check_balance():
    Account_Number = int(input("Enter your Account Number: "))
    if Account_Number in Account:
        print(f"Your current balance is: ${Account[Account_Number]['Initial_balance']:.2f}")
    else:
        print("Account number not found.")

# ---------------------- Save Transaction ----------------------- #
def save_transaction(Account_Number):
    if Account_Number in Account:
        with open("transactions.txt", "a") as file:
            for transaction in Account[Account_Number]["Transaction_History"]:
                file.write(f"{Account_Number}\t{transaction}\n")
        print("Transaction saved successfully.")
    else:
        print("Account not found")

# ---------------------- Transaction History -------------------- #
def Transaction_History():
    Account_Number = int(input("Enter your Account Number: "))
    if Account_Number not in Account:
        print("Account not found.\n")
        return
    Transaction = Account[Account_Number]["Transaction_History"]
    if not Transaction:
        print("No transactions found.")
        return
    for transaction in Transaction:
        print(transaction)
    save_transaction(Account_Number)

# ------------------------ Main Menu --------------------------- #
def Main_Menu():
    while True:
        print("\nMini Banking System\n")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit\n")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            Create_customer()
        elif choice == "2":
            Deposit_money()
        elif choice == "3":
            Withdraw_money()
        elif choice == "4":
            Check_balance()
        elif choice == "5":
            Transaction_History()
        elif choice == "6":
            print("Thank you for using the banking system.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")

Main_Menu()
bank