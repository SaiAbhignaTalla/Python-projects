print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
1500
tip_amount = bill*(tip/100)
bill_with_tip = bill + tip_amount
split = round(bill_with_tip / people ,2)

print(f"Each person should pay: {split}")