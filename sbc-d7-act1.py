import random

accounts = {} #dictionary to store info

def create_account():
    name = input("Enter your name: ")
    user_id = str(random.randint(00000, 99999)) #generate random user ID
    accounts[user_id] = {"name": name, "balance": 0.0}
    print(f"Account successfully created for {name} with user ID {user_id}")

def check_balance():
    user_id = input("Enter your user ID: ")
    if user_id in accounts:
        print(f"Balance for user ID {user_id}: {accounts[user_id]['balance']}")
    else:
        print("User ID not found")

def deposit():
    user_id = input("Enter your user ID: ")
    if user_id in accounts:
        amount = int(input("Enter amount to deposit: "))
        if amount < 0:  #if user enters a negative amount
            print("You cannot enter a negative amount")
            deposit() 
        else:
            accounts[user_id]["balance"] += amount
            print(f"Balance for user ID {user_id}: {accounts[user_id]['balance']}")
    else:
        print("User ID not found")

def withdraw():
    user_id = input("Enter your user ID: ")
    if user_id in accounts:
        amount = int(input("Enter amount to withdraw: "))
        if accounts[user_id]["balance"] >= amount:      # checks if current balance is greater than or equal to withdrawal
            print(f"Balance for user ID {user_id}: {accounts[user_id]['balance']}")
        else:
            print("Insufficient balance")
    else:
        print("User ID not found")

def delete_account():
    user_id = input("Enter your user ID: ")
    if user_id in accounts:
        del accounts[user_id]
        print(f"Account with user ID {user_id} deleted")
    else:
        print("User ID not found")

while True:
    print("\nWELCOME TO SBC BANK!")
    print("\nBank Menu:")
    print("1. Create Account | 2. Check Balance | 3. Deposit | 4. Withdraw | 5. Delete Account | 6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        check_balance()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        delete_account()
    elif choice == "6":
        break
    else:
        print("Invalid choice")