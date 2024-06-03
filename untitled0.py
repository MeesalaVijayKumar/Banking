from colorama import  Back
from colorama import Fore

# Python Banking Program

def show_balance(balance):
    print(Back.BLACK+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print(Fore.GREEN+f"  Your balance is Rs {balance:.2f}/-")
    print(Fore.RESET+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print()

def deposit():
    print(Back.BLACK+"*********************")
    amount = float(input(Fore.MAGENTA+"Enter an amount to be deposited: "))
    print(Fore.RESET+"*********************")
    if amount < 0:
        print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print(Fore.RED+"  That's not a valid amount")
        print(Fore.RESET+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print()
        return 0
    else:
        print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")       
        print(Fore.GREEN+f"  Successfully Rs {amount}/- deposited in your account")
        print(Fore.RESET+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print()
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input(Fore.MAGENTA+"Enter amount to be withdrawn: "))
    print(Fore.RESET+"*********************")

    if amount > balance:
        print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print(Fore.RED+"  Insufficient funds")
        print(Fore.RESET+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print()
        return 0
    elif amount < 0:
        print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print(Fore.RED+"  Amount must be greater than 0")
        print(Fore.RESET+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print()
        return 0
    else:
        print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")       
        print(Fore.GREEN+f"  Successfully Rs {amount}/- withdrawled from your account")
        print(Fore.RESET+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print()
        return amount

balance = 0
is_running = True

while is_running:
    print(Back.BLACK+"*********************")
    print("   Banking Program   ")
    print("*********************")
    print(Fore.GREEN+"1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print(Fore.RESET+"*********************")
    choice = input(Fore.MAGENTA +"Enter your choice (1-4): ")
    print(Fore.RESET+"")

    if choice == '1':
        show_balance(balance)
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw(balance)
    elif choice == '4':
        is_running = False
    else:
        print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print(Fore.RED+"  That is not a valid choice")
        print(Fore.RESET+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        print()

print(Back.BLACK+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
print(Fore.GREEN+"  Thank you! Have a nice day!")
print(Fore.RESET+"x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")



