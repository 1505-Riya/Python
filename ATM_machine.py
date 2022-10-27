#simulation of bank atm
#enter pin-->check balance,pay in,,make a withdrawal,return card
print("Welcome to atm")
restart=('y')
chances=3
balance=67.14

while chances>=0:
    pin=int(input("Please enter your four digit pin: "))
    if pin==(1234):
        print("You entered correct pin...\n")
        while restart not in ('n','N','NO','no'):
            print("Press 1 for your balance\n")
            print("Press 2 to make a withdrawl\n")
            print("Press 3 to pay in\n")
            print("Press 4 to return card\n")

            option=int(input("What would you like to choose?"))
            if option==1:
                print("Your balance is :",balance,'\n')
                restart=input("Would you like to go back?")
                if restart in ('n','N','NO','no'):
                    print("Thank you!")
                    break

            elif option==2:
                option2=('y')
                withdrawl=float(input("How much would you like to withdrawl?\n10/20/40/60/80/100"))
                if withdrawl in [10,20,40,60,80,100]:
                    balance=balance-withdrawl
                    print("Balance is now :",balance)
                    restart=input("Would you like to go back?")
                    if restart in ('n', 'N', 'NO', 'no'):
                        print("Thank you!")
                        break
                elif withdrawl != [10,20,40,60,80,100]:
                    print("Invalid amount,please re-try\n")
                    restart=('y')
                elif withdrawl==1:
                    withdrawl=float(input("enter desire amount:"))

            elif option==3:
                pay_in=float(input("How much would you like to pay in?"))
                balance=balance+pay_in
                print("\nBalance is now :", balance)
                restart = input("Would you like to go back?")
                if restart in ('n', 'N', 'NO', 'no'):
                    print("Thank you!")
                    break

            elif option==4:
                print("Please wait while your card is returned...\n")
                print("Thank you for your service")
                break

            else:
                print("Please enter a correct number,\n")
                restart=('y')
    elif pin!=('1234'):
        print("Incorrect pin")
        chances=chances-1
        if chances==0:
            print("No more tries")
            break







