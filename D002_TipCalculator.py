# num_char = len(input("What is your name?"))
# print(type(num_char))
# new_num_char = str(num_char)
# print(type(new_num_char))
# print("Your name has " + new_num_char + " characters.")    #function prints only similar datatype
# print(70 + float(100.5))
# print(str(70) + str(100))

# Mathematical operation:
# BEMDAS: () ** * / + -
# print(type(3/2))    this will give float type

#f-String: To combine all the datatype into string.
# score = 0
# height = 1.8
# isWinning = True
# #f-string
# print(f"Your score is {score}, height is {height}, winning is {isWinning}.")

#print(round(1.6666, 2))


#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator\nWhat was the final bill?")
final_bill_f = float(input())

print("How much would you like to give? 10, 12, or 15")
tip_i = float(input())

print("How many people to split the bill?")
total_people_i = int(input())

bill_with_tip_f = float(final_bill_f * (1 + tip_i / 100))
bill_with_tip_individual = bill_with_tip_f / total_people_i
# final_bill_with_tip_individual = round(bill_with_tip_individual,2)
final_bill_with_tip_individual = "{:.2f}".format(bill_with_tip_individual)

# print bill to pay for each person
print(f"Each person should pay: ${final_bill_with_tip_individual}")


