foods =[]
prices = []
total = []

while true:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
        print("------ YOUR CART ------")
        
        for food in foods:
            print(food, end = " ")
            total += price
            
        print("\n")
        print(f"Your totak is : R{total}")
        