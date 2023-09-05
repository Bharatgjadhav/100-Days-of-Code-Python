#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to the tip calculator")
restobill= float(input("what was the total bill $"))
tip_percentage= int(input("what percentage tip you would like to give? "))
number_people= int(input("how many people to spit the bill? "))

tip_amount_calculation = (tip_percentage/100) * restobill

total_amount_calculation = restobill + tip_amount_calculation 

each_person_to_pay_bill= round(total_amount_calculation / number_people,2)

print(f"each person should pay {each_person_to_pay_bill}")










#Age remainig calculator 

"""

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")







#total_days = int (365*90)
#total_month = int (48*90)
#total_weeks = int (12*90)

#spent_days = int(365* int(age))
#spent_month = int(12* int(age))
#spent_weeks = int(52 * int(age))


#remaining_days = total_days - spent_days
#remaining_month = total_month - spent_month
#remaining_week = total_weeks - spent_weeks

#print (f"days remainig {remaining_days} month remainig {remaining_month} weeks remaining {remaining_week}")

#print(f"You have {remaining_days} days, {remaining_week} weeks, and {remaining_month} months left.")
#print (f"days {total_days}, month left {total_month}, weeks left {total_week}")
"""