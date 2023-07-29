import random
class BankAccount:
    def __init__(self,name,phone,aadhar,pin,acc_no,balance):
        self.name = name
        self.phone=phone
        self.aadhar=aadhar
        self.pin=pin
        self.balance = balance
        self.acc_no=acc_no
    def deposit(self, amount):
        self.balance = self.balance+amount
        print("Deposit of ",amount,"successful. New balance is",self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Current balance is",self.balance)
        else:
            self.balance =self.balance-amount
            print("Withdrawal of",amount,"successful. New balance is",self.balance)
    def display_balance(self):
        print("Current balance for ",self.name,"is ",self.balance)
    def display_details(self):
        print("----------------------------------")
        print("Name: ",self.name)
        print("phone:",self.phone)
        print("Aadhar: ",self.aadhar)
        print("pin number: ",self.pin)
        print("Account no: ",self.acc_no)
        print("Balance Amount: ",self.balance)
        print("----------------------------------")
    def update_details(self):
        while (True):
            print("Choose your option :")
            print("1.update phone number")
            print("2.update pin number")
            print("3.Exit")
            ch = int(input())
            if ch==1:
                print("Enter the new phonenumber:")
                phone = int(input())
                accounts[name].phone=phone
                print("Phone number updated successfully")
            elif ch==2:
                print("Enter the new pin number:")
                pin = int(input())
                accounts[name].pin = pin
                print("Pin number updated successfully")
            elif ch==3:
                print("Thanks")
                break
            else:
                print("Invalid option")
    def close_account(self):
           print(self.name,"Account closed")
           accounts.pop(name)
accounts = {}
while True:
    print("########################")
    print("Banking Operations:")
    print("1. Open an account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5.Display details")
    print("6.update the details")
    print("7.Close Account")
    print("8. Exit")
    print("########################")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n=int(input("How many accounts you want to create:"))
        for i in range(0,n):
            name = input("Enter name: ")
            phone=int(input("Enter the phone no:"))
            aadhar=int(input("Enter the aadhar no"))
            pin=int(input("Enter the pin number:"))
            balance = int(input("Enter initial balance: "))
            acc_no=random.randint(10000,99999)
            bank=BankAccount(name,phone,aadhar,pin,acc_no,balance)
            accounts[name] =bank
            print("Account created for",name, "successfully.")
            print("your account number is",acc_no)
            print("-------------------------")
    elif choice == 2:
        name = input("Enter name: ")
        if name not in accounts:
            print("No account exists for ",name)
        else:
            acc_temp=int(input("Enter the account no:"))
            if accounts[name].acc_no==acc_temp:
                amount = int(input("Enter deposit amount: "))
                accounts[name].deposit(amount)
            else:
                print("your account number is invalid")
    elif choice == 3:
        name = input("Enter name: ")
        if name not in accounts:
            print("No account exists for",name)
        else:
            acc_temp = int(input("Enter the account no:"))
            if accounts[name].acc_no == acc_temp:
                amount = int(input("Enter withdrawal amount: "))
                accounts[name].withdraw(amount)
            else:
                print("your account number is invalid")
    elif choice == 4:
        name = input("Enter name: ")
        if name not in accounts:
            print("No account exists for",name)
        else:
            acc_temp = int(input("Enter the account no:"))
            if accounts[name].acc_no == acc_temp:
                accounts[name].display_balance()
    elif choice==5:
        for x in accounts:
            accounts[x].display_details()
    elif choice == 6:
        name = input("Enter the name:")
        if name not in accounts:
            print("No account exists for", name)
        else:
            accounts[name].update_details()
    elif choice==7:
        name=input("Enter the name of whose account want to be close:")
        if name not in accounts:
            print("No account exists for",name)
        else:
            acc_temp = int(input("Enter the account no:"))
            if accounts[name].acc_no == acc_temp:
                accounts[name].close_account()
            else:
                print("your account number is invalid")
    elif choice == 8:
        print("Thank you for using our banking system.")
        break
    else:
        print("Invalid choice. Please try again.")
