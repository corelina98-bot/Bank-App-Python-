class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return True
        else:
            print("Deposit amount must be non-negative")
            return False
            
    def withdraw(self, amount):
        if amount >= 0:
            if self.balance >= amount:
                self.balance -= amount
                return True
            else:
                print("Insufficient balance")
                return False
        else:
            print("Withdrawal amount must be non-negative")
            return False
            
    def transfer(self, other_account, amount):
        if amount >= 0:
            if self.balance >= amount:
                self.balance -= amount
                other_account.balance += amount
                return True
            else:
                print("Insufficient balance")
                return False
        else:
            print("Transfer amount must be non-negative")
            return False
            
    def check_balance(self):
        return self.balance
        
def create_account(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Account already exists")
        return
    initial_balance = float(input("Enter initial balance: "))
    accounts[account_number] = BankAccount(account_number, initial_balance)
    print("Account created successfully")   
        
def deposit(accounts):
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account does not exist")
        return
    amount = float(input("Enter deposit amount: "))
    accounts[account_number].deposit(amount)
    
def withdraw(accounts):
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account does not exist")
        return
    amount = float(input("Enter withdrawal amount: "))
    accounts[account_number].withdraw(amount)
    
def transfer(accounts):
    from_account = input("Enter source account number: ")
    to_account = input("Enter target account number: ")
    if from_account not in accounts or to_account not in accounts:
        print("One or both accounts do not exist")
        return
    amount = float(input("Enter transfer amount: "))
    accounts[from_account].transfer(accounts[to_account], amount)
    
def check_balance(accounts):
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Account does not exist")
        return
    balance = accounts[account_number].check_balance()
    print("Current balance: ", balance)
    
def main():
    accounts = {}
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Check Balance\n6. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            transfer(accounts)
        elif choice == '5':
            check_balance(accounts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
    