class Account_management:
    def __init__(self,name,account_no,balance):
        self.name = name
        self.account = account_no
        self.balance = balance
    def creating(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print(" deposit amount must be positive ")
    def updating(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance:{self.balance}")
            else:
                print("Amount is empty.")
        else:
            print("Withdrawal amount must be positive")
    def __str__(self):
        return f"Account user: {self.name}\nAccount No:{self.account}\nBalance: {self.balance}"
if __name__ == "__main__":
    account = Account_management("Muhammad umair",12345,2000)
    print(account)
    account.creating(500)
    account.updating(200)
    account.updating(1500)