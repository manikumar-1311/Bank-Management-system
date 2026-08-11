def deposit():
    amount = int(input("Enter your amount: ")) # 500
    if amount > 0:
        print(f'Amount {amount}/- Credited Successfully!')
        return amount
    else:
        print('Invalid Amount!')
        return 0

def withdraw():
    amount = int(input("Enter your amount: ")) # 400
    if balance >= amount:
        print(f'Amount {amount}/- Debited Successfully!')
        return amount
    else:
        print('Insufficient Fund!')
        return 0

def check_balance():
    print(f'Your Current Balance is: {balance}')

def check_credentials():
    db_pin = 1289
    chances = 3
    for i in range(1,chances+1):
        input_pin = int(input("Enter your pin: "))
        if db_pin == input_pin:
            return True
        else:
            if chances-i != 0:
                print(f'Wrong pin, You have only {chances-i} chances left!')
            else:
                return False

print('<----- WELCOME TO BANK MANAGEMENT SYSTEM ----->')
balance = 0.0
if check_credentials() == True:
    while True:
        print('\n1) DEPOSIT')
        print('2) WITHDRAW')
        print('3) CHECK BALANCE')
        print('4) EXIT')

        choice = int(input('Enter your choice: '))
        match choice:
            case 1: balance += deposit()
            case 2: balance -= withdraw()
            case 3: check_balance()
            case 4: 
                print('THANK YOU, VISIT AGAIN!')
                break
            case _: print('Invalid Choice, Try again..!')
else:
    print('Too many Attempts, you need to wait for 24hrs!')
