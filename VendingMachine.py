# You are tasked to code the vending machine logic out using Python Programming Language. 
# In your code, you can have a few drinks as your items with any price (no coin). 
# The customer should be able to insert any notes to buy his preferred drinks. 
# The outcome is to release the least amount of notes back to the customer. 

drinks = ['Coke', 'Sprite', 'Pepsi']
prices = [1, 2, 3]

print("\n****WELCOME TO VENDING MACHINE****\n")
print('Available Drinks:')

for i in range(len(drinks)):
        print(f'{i+1}. {drinks[i]} \t- ${prices[i]}')

print()

totalCost = 0
while(True):
    drinkChoice = int(input(f"Enter selection 1-3 (0 to stop): \n"))
    if drinkChoice == 0: break
    while(drinkChoice>3):
            print('Invalid input!')
            drinkChoice = int(input(f"Enter selection 1-3 (0 to stop): \n"))
            if drinkChoice == 0: break
    print('You have selected: ' + drinks[drinkChoice-1])
    totalCost += prices[drinkChoice-1]
        
print('-----------------------------')
print("Total cost = $",totalCost)
cash = int(input("Enter cash notes: $"))
while(cash<totalCost):
    print("Insufficient cash!")
    cash = int(input("Enter cash notes: $"))
change = cash - totalCost
print("Your change = $",change)
print('-----------------------------')
print('Change given:')
print(f'$1 \tx {int(change%10%5)}')
print(f'$5 \tx {int(change%10/5)}')
print(f'$10 \tx {int(change%100/10%5%2)}')
print(f'$20 \tx {int(change%100/10%5/2)}')
print(f'$50 \tx {int(change%100/10/5)}')
print(f'$100 \tx {int(change%1000/100)}')
print('-----------------------------')
print("Thank you for your purchase!")
print('-----------------------------')
