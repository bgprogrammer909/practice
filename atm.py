balance=10000
print("Welcome to ATM  \n 1.balanace inquiry \n 2.withdraw cash \n 3.deposit cash \n 4.exit")
choice=int(input('Please enter your choice: '))
if choice==1:
    print(f'your current balance is {balance}')
elif choice==2:
    amount=int(input('enter the amount that you want to withdraw: '))
    if amount>balance:
        print('insufficient balance.')
    else:
        balance-=amount
        print(f'withdraw successful, new balance is {balance}')
elif choice==3:
    amount=int(input('Enter the amount you want to deposit: '))
    if amount<=0:
        print('Invalid input, enter positive number')
    else:
        balance+=amount
        print(f'Deposit successful, new balnce is {balance}.')
elif choice==4:
    print("Thankn you for using the ATM. Goodbye!")
else:
    print("Invalid choice. please try again.")
