balance = 9999999999

#Options: 1. check balance 2. withdraw money 3. deposit money 4. exit

while True:    
        
        x = input("Choose an option (1-4)")    
        if x == '1':
                        print(f"Your current balance is: ${balance}")
                
        elif x == '2':
                money = float(input(f"How much would you like to withdraw? "))
                if money < 0:
                        print("Error: Cannot withdraw a negative money.")
                elif money > balance:
                        print("Error: Insufficient funds.")
                else:
                        balance -= money
                        print(f"You have withdrawn {money}")
                
        elif x == '3':
                money = float(input(f"How much deposit"))
                if money < 0:
                        print("Cannot deposit a negative")
                else:
                        balance += money
                        print(f"You have deposited {money}")    
        elif x == '4':
                print("Exiting")
                break
        else:
                print("Choose a number between 1 and 4.")
