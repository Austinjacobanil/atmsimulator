'''Python programe to replicate the working of ATM for a single user, let’s say, Mr. John, who has already 
successfully logged into her account on the ATM Machine, now, we will program the next steps 
he may want to perform.
Like display his name and cash available in his savings account
Withdraw cash and display the status of the cash balance.
Deposit cash and display the status of the cash balance.
(Your task is to design and implement the ATM functionality by taking care of all constraints, for 
example if minimum cash available is less than 5000 then system will display low balance)'''


print("Hey!!! John, welcome to ATM service")
print("                                ")
balance=10000
'''instruction to operate the ATM.'''
print("Enter 1 to Check balance")
print("Enter 2 to  Withdraw")
print("Enter 3 to Deposit")
''' to give space'''
print(" ")
number=int(input("Enter your response: "))
if number==1:
    print("Your current balance is:",balance)
    print("!!Thankyou!!")
elif number==2:
    withdraw_amount=int(input("Enter the amount to withdraw: "))
    if withdraw_amount<=10000:
        current_balance=balance-withdraw_amount
        print("You succesfully withdrawn",withdraw_amount)
        print("Your current balance is:",current_balance)
        if current_balance<=5000:
            print("!!! your current balance is low !!!")
    else:
        print("Insufficient balance")
elif number==3:
    deposit_amount=int(input("Enter the amount to deposit:  "))
    current_balance=balance+deposit_amount
    print("You succesfully deposited",deposit_amount)
    print("Your current balance is:",current_balance)
else:
    print("Invalid response")
