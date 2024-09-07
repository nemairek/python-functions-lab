# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.

#def calculate_area_triangle(b, h):
    #return b/2 * h 

#print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.

#def simple_interest(p, r, t):
#    return p * r/100 * t

#print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.

#def apply_discount(p, d):
#    return p * (1 - d/100)

#print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.

# def convert_temperature(t, u):
#     if u == 'C':
#         return (t * 9/5) + 32
#     elif u == 'F':
#         return (t - 32) * 5/9
#     else:
#         return('invalid entry')

# print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
# print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.
# def sum_to(n):
#     return n/2 * (1 + n)


# print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
# def largest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     elif c > b and c > a:
#         return c
# print('Exercise 6:', largest(1, 2, 3))

# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.
# def calculate_tip(b, p):
#     return b * (p/100)



# print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.
# def product(*nu):
#     result = 1
#     for n in nu:
#         result *= n
#     return result


# print('Exercise 8:', product(2, 5, 5))

# Exercise 9: Basic Calculator
#
# Create a function named `basicCalculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basicCalculator(10, 5, 'subtract') should return 5.
# basicCalculator(10, 5, 'add') should return 15.
# basicCalculator(10, 5, 'multiply') should return 50.
# basicCalculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.
def basicCalculator(n1, n2, o):
    if o == 'add':
        return n1 + n2
    elif o == 'subtract':
        return n1 - n2
    elif o == 'multiply':
        return n1 * n2
    elif o == 'divide':
        return n1/n2

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))
