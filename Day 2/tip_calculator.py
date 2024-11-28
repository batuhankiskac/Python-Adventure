print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15? "))
person_count = int(input("How many people to split the bill? "))
tip = bill / 100 * tip_percent / person_count
print(f"Each person should pay : ${round(tip, 2)}")
