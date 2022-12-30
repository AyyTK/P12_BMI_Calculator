# Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
# It’s calculated using a person's weight and height, using this formula: weight / height²
#
# The resulting number indicates one of the following categories:
# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more
#
# Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's
# weight and height as input and outputs the corresponding BMI category.

height1 = float(input("Type your height here in CM "))
weight = float(input("Type your weight here in KG "))

height2 = height1 ** 2

bmi = weight / height2
bmi2 = bmi * 10000

print(bmi2)

if bmi2 < 18.5:
    print("Underweight")
elif 18.5 <= bmi2 < 25:
    print("Normal")
elif 25 <= bmi2 < 30:
    print("Overweight")
else:
    print("Obese")