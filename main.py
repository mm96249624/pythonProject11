# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# <stdio.h>
# <cs50.h>

def year():
	currentyear = int(input("Enter the current year: "))
	currentmonth = int(input("Enter the number of the current month: "))
	birthyear = int(input("Enter the birth year: "))
	birthmonth = int(input("Enter the number of the birth month: "))
	age = (currentyear - birthyear) * 12 + (currentmonth - birthmonth)
	return age

print("Your age in months:",year())
name=input("Name on your bank account? ")
balance=float(input("Your current balance? "))

def printMenu():
    print(name,"Welcome to the Lots of Money Bank")
    print("Enter 'b'(balance), 'd'(deposit), 'w'(withdraw), or'q'(quit)")

def getTransaction():
    transaction=str(input("What would you like to do? "))
    return transaction

def withdraw(bal,amt):
    global balance
    balance=bal-amt
    if balance<0:
        balance=balance-10
