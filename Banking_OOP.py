# Banking System
# Parent Class: User
# Holds details about the user
# Has a function to show all the details
# Child Class:
# Stores details about the account balance 
# Stores the details about the amount
# Allow deposite withdraw and veiw balance.

#Parent class
class User:
    def __init__(self, name, age, gender): #holds details about the users
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print("<<<Personel Details>>>\n")
        print(f"Name  {self.name}\nAge  {self.age}\nGender  {self.gender}")


#Child Class
class Bank(User):
     def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

     def deposite(self, amount):
        self.balance+=amount
        print(f"\n{amount} deposited >>> Updated Balance $ {self.balance}")

     def withdraw(self, amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f"{amount} withdrawn >>> Updated Balance $ {self.balance}\n")
        else:
            print(f"Insufficient Balnce! | Balance Available {self.balance}\n")

     def veiw_balance(self):
        self.details()
        print(f"Account Balance $ {self.balance}")

   

sam = Bank("Sam", 25, "Male")
sam.deposite(100)
sam.withdraw(20)
sam.veiw_balance()





