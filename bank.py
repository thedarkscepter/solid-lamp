class Bank:
    def __init__(self, card_number, card_pin):
        self.card_number = card_number
        self.card_pin = card_pin

    def check_balance(self):
        print("YOUR BALANCE IS $10000000000000!!!")

    def withdraw_cash(self, amount):
        new_amount = 10000000000000 - amount
        print("YOU HAVE WITHDRAWN $10000000000000!!! " + str(amount) + "your current balance is " + str(new_amount))
def main():
    card_number = input("ENTER YOUR CARD NUMBER!!! ")
    card_pin = input("ENTER YPUR PIN!!! ")
    new_user = Bank(card_number, card_pin)
    print("CHOOSE YOUR ACTIVITIES!!! ")
    print("1. BALANCE INQUIRY!  2. WITHDRAWL! ")
    activity = int(input("ENTER ACTIVITY NUMBER!!!"))
    
    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("ENTER THE AMOUNT!!!!! "))
        new_user.withdraw_cash(amount)
    else:
        print("ENTER A VALID NUMBER!!!!")

if __name__ == "__main__":
    main()