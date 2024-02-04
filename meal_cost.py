meal_cost = float(input( "Enter the cost of the meal"))
sales_tax =0.07*meal_cost
tip = 0.18*meal_cost


tip_amount =tip/100*meal_cost #calculates the tip amount
total_meal_cost =meal_cost+sales_tax+tip_amount
print("The cost of your meal is: Ksh{:.2f}".format (meal_cost)) 
print("Total taxes is: Ksh {:.2f}".format (sales_tax)) 
print("The tip is: Ksh {:.2f}" .format (tip_amount))
print("The total cost of your meal is: Ksh {:.2f}".format (total_meal_cost)) 
