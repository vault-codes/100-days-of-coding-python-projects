print("Welcome to the Tip calculator!")

total_bill = int(input("What was the total bill $ ?"))


tip = int(input("How much tip will you like to give? 10, 12 or 15?"))

tip /= 100

tip_amount = total_bill * tip

total_bill += tip_amount

no_of_people = int(input("How many people are spliting the bill?"))

each_bill = round(total_bill/no_of_people, 2)

print(f"Each person is to pay: {each_bill} ")