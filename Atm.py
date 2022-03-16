class Atm(object):
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.money = 100
    
    def cashWithdrawal(self, amount):
        if amount > self.money:
            print("Insufficient balance!")
        else:
            self.money -= amount
            print("Money withdrawn")
    
    def bankEnquiry(self):
        print('₹' + str(self.money))

cardnumber = input("Enter card number: ")
pin = input("Enter pin number: ")
person1 = Atm(cardnumber, pin)
operation = input("Enter operation(Withdrawal, Enquiry): ")

if operation == 'Withdrawal':
    amount = int(input("Enter the amount: "))
    person1.cashWithdrawal(amount)
elif operation == 'Enquiry':
    person1.bankEnquiry()
else:
    print("Operation invalid!!")
