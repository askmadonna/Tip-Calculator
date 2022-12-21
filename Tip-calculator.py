#If the bill was $150.00, split between 5 people, with 12% tip.
bill = int(input("enter bill\n"))
split_bill = bill / 5
print(split_bill)

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
person_split = (bill / 5) * 1.12
ps = round(person_split)
print(f"each person should pay {ps}")
