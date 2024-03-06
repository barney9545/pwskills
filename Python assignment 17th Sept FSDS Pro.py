# Print numbers from 1 to 10 using a for loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# Difference between a for loop and a while loop
# For loop: Used when you know the number of iterations in advance.
# While loop: Used when you don't know the number of iterations in advance, and the loop continues until a condition is met.

# Calculate the sum of all numbers from 1 to 100 using a for loop
sum_of_numbers = 0
for i in range(1, 101):
    sum_of_numbers += i
print("Sum of numbers from 1 to 100:", sum_of_numbers)

# Iterate through a list using a for loop
my_list = [1, 2, 3, 4, 5]
print("Iterating through a list using a for loop:")
for item in my_list:
    print(item, end=" ")
print()

# Find the product of all elements in a list using a for loop
product = 1
for num in my_list:
    product *= num
print("Product of elements in the list:", product)

# Print all even numbers from 1 to 20 using a for loop
print("Even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Calculate the factorial of a number using a for loop
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, ":", factorial)

# Iterate through the characters of a string using a for loop
my_string = "Hello"
print("Characters of the string:", my_string)
for char in my_string:
    print(char, end=" ")
print()

# Find the largest number in a list using a for loop
numbers = [5, 8, 2, 10, 3]
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
print("Largest number in the list:", max_number)

# Print the Fibonacci sequence up to a specified limit using a for loop
limit = 10
a, b = 0, 1
print("Fibonacci sequence up to", limit, ":")
for _ in range(limit):
    print(a, end=" ")
    a, b = b, a + b
print()

# Count the number of vowels in a given string using a for loop
vowels = 'aeiou'
sentence = "Hello, how are you?"
count = 0
for char in sentence:
    if char.lower() in vowels:
        count += 1
print("Number of vowels in the string:", count)

# Generate a multiplication table for a given number using a for loop
num = 5
print("Multiplication table for", num, ":")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Reverse a list using a for loop
my_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print("Reversed list:", reversed_list)

# Find the common elements between two lists using a for loop
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []
for item in list1:
    if item in list2:
        common_elements.append(item)
print("Common elements between the two lists:", common_elements)

# Iterate through the keys and values of a dictionary using a for loop
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Iterating through keys and values of the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)

# Find the GCD (Greatest Common Divisor) of two numbers using a for loop
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 12
num2 = 18
print("GCD of", num1, "and", num2, ":", gcd(num1, num2))

# Check if a string is a palindrome using a for loop
def is_palindrome(s):
    s = s.lower()
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

my_string = "radar"
print("Is", my_string, "a palindrome?", is_palindrome(my_string))

# Remove duplicates from a list using a for loop
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicates:", unique_list)

# Count the number of words in a sentence using a for loop
sentence = "This is a sample sentence."
word_count = 0
for _ in sentence.split():
    word_count += 1
print("Number of words in the sentence:", word_count)

# Find the sum of all odd numbers from 1 to 50 using a for loop
sum_of_odd = 0
for i in range(1, 51, 2):
    sum_of_odd += i
print("Sum of odd numbers from 1 to 50:", sum_of_odd)

# Check if a given year is a leap year using a for loop
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = 2024
print(year, "is a leap year?" , is_leap_year(year))

# Calculate the square root of a number using a for loop
def square_root(num):
    guess = num / 2
    for _ in range(10):
        guess = (guess + num / guess) / 2
    return guess

number = 25
print("Square root of", number, ":", square_root(number))

# Find the LCM (Least Common Multiple) of two numbers using a for loop
def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm

num1 = 12
num2 = 15
print("LCM of", num1, "and", num2, ":", lcm(num1, num2))


# Check if a number is positive, negative, or zero using if-else statement
number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Check if a given number is even or odd using if-else statement
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Nested if-else statements in Python
# Nested if-else statements are used to create conditional branches within other conditional branches.
# Example:
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Determine the largest of three numbers using if-else
a, b, c = 5, 10, 3
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest of", a, ",", b, ", and", c, "is", largest)

# Calculate the absolute value of a number using if-else
number = -7
if number < 0:
    absolute_value = -number
else:
    absolute_value = number
print("Absolute value of", number, "is", absolute_value)

# Check if a given character is a vowel or consonant using if-else
char = 'a'
if char.lower() in 'aeiou':
    print(char, "is a vowel")
else:
    print(char, "is a consonant")

# Determine if a user is eligible to vote based on their age using if-else
age = 20
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Calculate the discount amount based on the purchase amount using if-else
purchase_amount = 200
if purchase_amount >= 100:
    discount = 10
else:
    discount = 0
print("Discount amount:", discount)

# Check if a number is within a specified range using if-else
number = 25
if number >= 10 and number <= 30:
    print(number, "is within the specified range")
else:
    print(number, "is not within the specified range")

# Determine the grade of a student based on their score using if-else
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)

# Check if a string is empty or not using if-else
string = ""
if string:
    print("String is not empty")
else:
    print("String is empty")

# Identify the type of a triangle based on input values using if-else
a, b, c = 3, 4, 5
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# Determine the day of the week based on a user-provided number using if-else
day_number = 3
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid day number")

# Check if a given year is a leap year using both if-else and a function
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = 2024
if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Use the "assert" statement in Python to add debugging checks within if-else blocks
age = 65
assert age >= 60, "Age must be greater than or equal to 60 for senior citizen discount"
print("You are eligible for a senior citizen discount")

# Determine the eligibility of a person for a senior citizen discount based on age using if-else
age = 70
if age >= 60:
    print("You are eligible for a senior citizen discount")
else:
    print("You are not eligible for a senior citizen discount")

# Categorize a given character as uppercase, lowercase, or neither using if-else
char = 'A'
if char.isupper():
    print(char, "is uppercase")
elif char.islower():
    print(char, "is lowercase")
else:
    print(char, "is neither uppercase nor lowercase")

# Determine the roots of a quadratic equation using if-else
import math
a, b, c = 1, -3, 2
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots are real and distinct:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("Roots are real and equal:", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print("Roots are complex:", real_part, "+", imaginary_part, "i and", real_part, "-", imaginary_part, "i")

# Check if a given year is a century year or not using if-else
year = 1900
if year % 100 == 0:
    print(year, "is a century year")
else:
    print(year, "is not a century year")

# Determine if a given number is a perfect square using if-else
number = 25
sqrt = math.sqrt(number)
if sqrt == int(sqrt):
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")

# Purpose of "continue" and "break" statements within if-else loops:
# "continue": Skips the rest of the loop's code for the current iteration and proceeds to the next iteration.
# "break": Exits the loop immediately, skipping any remaining iterations.

# Calculate the BMI (Body Mass Index) of a person based on their weight and height using if-else
weight = 70 # in kilograms
height = 1.75 # in meters
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Use the "filter()" function with if-else statements to filter elements from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers in the list:", list(filtered_numbers))

# Determine if a given number is prime or not using if-else
number = 17
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
# Check if a number is positive, negative, or zero using if-else statement
number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Check if a given number is even or odd using if-else statement
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Nested if-else statements in Python
# Nested if-else statements are used to create conditional branches within other conditional branches.
# Example:
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Determine the largest of three numbers using if-else
a, b, c = 5, 10, 3
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest of", a, ",", b, ", and", c, "is", largest)

# Calculate the absolute value of a number using if-else
number = -7
if number < 0:
    absolute_value = -number
else:
    absolute_value = number
print("Absolute value of", number, "is", absolute_value)

# Check if a given character is a vowel or consonant using if-else
char = 'a'
if char.lower() in 'aeiou':
    print(char, "is a vowel")
else:
    print(char, "is a consonant")

# Determine if a user is eligible to vote based on their age using if-else
age = 20
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Calculate the discount amount based on the purchase amount using if-else
purchase_amount = 200
if purchase_amount >= 100:
    discount = 10
else:
    discount = 0
print("Discount amount:", discount)

# Check if a number is within a specified range using if-else
number = 25
if number >= 10 and number <= 30:
    print(number, "is within the specified range")
else:
    print(number, "is not within the specified range")

# Determine the grade of a student based on their score using if-else
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)

# Check if a string is empty or not using if-else
string = ""
if string:
    print("String is not empty")
else:
    print("String is empty")

# Identify the type of a triangle based on input values using if-else
a, b, c = 3, 4, 5
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# Determine the day of the week based on a user-provided number using if-else
day_number = 3
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid day number")

# Check if a given year is a leap year using both if-else and a function
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = 2024
if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Use the "assert" statement in Python to add debugging checks within if-else blocks
age = 65
assert age >= 60, "Age must be greater than or equal to 60 for senior citizen discount"
print("You are eligible for a senior citizen discount")

# Determine the eligibility of a person for a senior citizen discount based on age using if-else
age = 70
if age >= 60:
    print("You are eligible for a senior citizen discount")
else:
    print("You are not eligible for a senior citizen discount")

# Categorize a given character as uppercase, lowercase, or neither using if-else
char = 'A'
if char.isupper():
    print(char, "is uppercase")
elif char.islower():
    print(char, "is lowercase")
else:
    print(char, "is neither uppercase nor lowercase")

# Determine the roots of a quadratic equation using if-else
import math
a, b, c = 1, -3, 2
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots are real and distinct:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("Roots are real and equal:", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print("Roots are complex:", real_part, "+", imaginary_part, "i and", real_part, "-", imaginary_part, "i")

# Check if a given year is a century year or not using if-else
year = 1900
if year % 100 == 0:
    print(year, "is a century year")
else:
    print(year, "is not a century year")

# Determine if a given number is a perfect square using if-else
number = 25
sqrt = math.sqrt(number)
if sqrt == int(sqrt):
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")

# Purpose of "continue" and "break" statements within if-else loops:
# "continue": Skips the rest of the loop's code for the current iteration and proceeds to the next iteration.
# "break": Exits the loop immediately, skipping any remaining iterations.

# Calculate the BMI (Body Mass Index) of a person based on their weight and height using if-else
weight = 70 # in kilograms
height = 1.75 # in meters
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Use the "filter()" function with if-else statements to filter elements from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers in the list:", list(filtered_numbers))

# Determine if a given number is prime or not using if-else
number = 17
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# 1. Explain the purpose of the `map()` function and provide an example.
# The `map()` function in Python is used to apply a specified function to each item in an iterable (such as a list) and returns an iterator that yields the results.
# Example:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# 2. Write a Python program that uses the `map()` function to square each element of a list of numbers.
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# 3. How does the `map()` function differ from a list comprehension in Python, and when would you choose one over the other?
# The `map()` function and list comprehensions are both used to apply a function to each element of an iterable, but list comprehensions are often more readable and concise for simple operations.
# `map()` is more appropriate when the operation is complex or when you already have a function defined that you want to apply.
# List comprehensions are more Pythonic and are often preferred for their readability.
# Example:
# Using list comprehension:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# 4. Create a Python program that uses the `map()` function to convert a list of names to uppercase.
names = ['alice', 'bob', 'charlie']
uppercase_names = map(str.upper, names)
print(list(uppercase_names))  # Output: ['ALICE', 'BOB', 'CHARLIE']

# 5. Write a Python program that uses the `map()` function to calculate the length of each word in a list of strings.
words = ['apple', 'banana', 'orange']
word_lengths = map(len, words)
print(list(word_lengths))  # Output: [5, 6, 6]

# 6. How can you use the `map()` function to apply a custom function to elements of multiple lists simultaneously in Python?
# You can pass multiple iterable arguments to the `map()` function, along with the custom function that takes corresponding elements from each iterable as its arguments.
# Example:
def add(a, b):
    return a + b

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(add, list1, list2)
print(list(result))  # Output: [5, 7, 9]

# 7. Create a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.
temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = map(lambda c: c * 9/5 + 32, temperatures_celsius)
print(list(temperatures_fahrenheit))  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]

# 8. Write a Python program that uses the `map()` function to round each element of a list of floating-point numbers to the nearest integer.
float_numbers = [3.14, 2.718, 1.618]
rounded_numbers = map(round, float_numbers)
print(list(rounded_numbers))  # Output: [3, 3, 2]


# 1. What is the `reduce()` function in Python, and what module should you import to use it?
# The `reduce()` function in Python is used to apply a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
# You need to import the `functools` module to use it.
# Example of basic usage:
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# 2. Write a Python program that uses the `reduce()` function to find the product of all elements in a list.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# 3. Create a Python program that uses `reduce()` to find the maximum element in a list of numbers.
from functools import reduce

numbers = [1, 6, 3, 8, 2]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)  # Output: 8

# 4. How can you use the `reduce()` function to concatenate a list of strings into a single string?
# You can use the `reduce()` function with the concatenation operator (`+`).
# Example:
from functools import reduce

strings = ['hello', 'world', 'python']
concatenated_string = reduce(lambda x, y: x + y, strings)
print(concatenated_string)  # Output: helloworldpython

# 5. Write a Python program that calculates the factorial of a number using the `reduce()` function.
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

print(factorial(5))  # Output: 120

# 6. Create a Python program that uses `reduce()` to find the GCD (Greatest Common Divisor) of a list of numbers.
from functools import reduce
import math

numbers = [24, 36, 48]
gcd = reduce(math.gcd, numbers)
print(gcd)  # Output: 12

# 7. Write a Python program that uses the `reduce()` function to find the sum of the digits of a given number.
from functools import reduce

def sum_of_digits(number):
    return reduce(lambda x, y: int(x) + int(y), str(number))

print(sum_of_digits(12345))  # Output: 15


#recursion

# 1. Explain the concept of recursion in Python. How does it differ from iteration?
# Recursion is a programming technique where a function calls itself to solve a problem. In recursion, the solution to the base case is provided explicitly, while the solution to the larger problem is expressed in terms of smaller instances of the same problem.
# Recursion differs from iteration in that iteration uses loops to repeat a set of instructions, whereas recursion calls itself repeatedly to solve smaller instances of the problem until a base case is reached.

# 2. Write a Python program to calculate the factorial of a number using recursion.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 3. Create a recursive Python function to find the nth Fibonacci number.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # Output: 13

# 4. Write a recursive Python function to calculate the sum of all elements in a list.
def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

print(recursive_sum([1, 2, 3, 4, 5]))  # Output: 15

# 5. How can you prevent a recursive function from running indefinitely, causing a stack overflow error?
# To prevent a recursive function from running indefinitely, you should ensure that there is a base case that will eventually terminate the recursion. 
# Additionally, you can set a maximum recursion depth using the sys module's setrecursionlimit() function or by using an iterative approach instead of recursion if applicable.

# 6. Create a recursive Python function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(24, 36))  # Output: 12

# 7. Write a recursive Python function to reverse a string.
def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # Output: "olleh"

# 8. Create a recursive Python function to calculate the power of a number (x^n).
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2, 3))  # Output: 8

# 9. Write a recursive Python function to find all permutations of a given string.
def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            for perm in permutations(s[:i] + s[i+1:]):
                perms.append(c + perm)
        return perms

print(permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# 10. Write a recursive Python function to check if a string is a palindrome.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # Output: True

# 11. Create a recursive Python function to generate all possible combinations of a list of elements.
def combinations(lst):
    if not lst:
        return [[]]
    else:
        head = lst[0]
        tail_combinations = combinations(lst[1:])
        return tail_combinations + [[head] + combination for combination in tail_combinations]

print(combinations([1, 2, 3]))  # Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]


#Basic functions

# 1. What is a function in Python, and why is it used?
# A function in Python is a block of reusable code that performs a specific task. It is used to organize code into manageable and reusable chunks, improve code readability, and promote code reusability.

# 2. How do you define a function in Python? Provide an example.
# You define a function in Python using the `def` keyword followed by the function name and parameters (if any). The function body contains the code to be executed when the function is called.
# Example:
def greet(name):
    print("Hello, " + name)

# 3. Explain the difference between a function definition and a function call.
# A function definition is where you define the structure and behavior of a function, including its name, parameters, and code block. A function call, on the other hand, is when you execute or invoke the function with specific arguments.

# 4. Write a Python program that defines a function to calculate the sum of two numbers and then calls the function.
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# 5. What is a function signature, and what information does it typically include?
# A function signature in Python typically includes the function name, parameters (including their types and order), and return type. It serves as a unique identifier for the function, allowing other code to understand how to interact with it.

# 6. Create a Python function that takes two arguments and returns their product.
def product(a, b):
    return a * b

print(product(4, 6))  # Output: 24


#Function Parameters and Arguments:
# 1. Explain the concepts of formal parameters and actual arguments in Python functions.
# Formal parameters refer to the parameters defined in the function signature or definition. They act as placeholders for the values that will be passed into the function during function calls.
# Actual arguments, on the other hand, are the values provided to the function when it is called. These values are assigned to the formal parameters defined in the function.

# 2. Write a Python program that defines a function with default argument values.
def greet(name="World"):
    print("Hello, " + name)

greet()  # Output: Hello, World
greet("Alice")  # Output: Hello, Alice

# 3. How do you use keyword arguments in Python function calls? Provide an example.
# Keyword arguments allow you to specify arguments by their parameter names when calling a function, which can improve code readability.
# Example:
def greet(name, greeting="Hello"):
    print(greeting + ", " + name)

greet(name="Alice", greeting="Hi")  # Output: Hi, Alice

# 4. Create a Python function that accepts a variable number of arguments and calculates their sum.
def sum_values(*args):
    return sum(args)

print(sum_values(1, 2, 3, 4, 5))  # Output: 15

# 5. What is the purpose of the `*args` and `**kwargs` syntax in function parameter lists?
# The `*args` syntax in function parameter lists allows a function to accept a variable number of positional arguments, while the `**kwargs` syntax allows it to accept a variable number of keyword arguments.
# `*args` collects extra positional arguments into a tuple, and `**kwargs` collects extra keyword arguments into a dictionary. This flexibility enables functions to handle a wide range of inputs without explicitly defining every parameter.


##Return Values and Scoping:


# 1. Describe the role of the `return` statement in Python functions and provide examples.
# The `return` statement is used to exit a function and return a value to the caller. It can also be used to return multiple values as a tuple. If there is no `return` statement, the function returns `None` by default.
# Example:
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# 2. Explain the concept of variable scope in Python, including local and global variables.
# Variable scope refers to the visibility of variables within different parts of a program. In Python, variables can have local or global scope.
# Local variables are defined within a function and are only accessible within that function.
# Global variables are defined outside of any function and can be accessed and modified by any part of the code.

# 3. Write a Python program that demonstrates the use of global variables within functions.
global_var = 10

def modify_global():
    global global_var
    global_var += 5
    print("Inside function:", global_var)

modify_global()
print("Outside function:", global_var)  # Output: Inside function: 15   Outside function: 15

# 4. Create a Python function that calculates the factorial of a number and returns it.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 5. How can you access variables defined outside a function from within the function?
# You can access variables defined outside a function from within the function by using the `global` keyword to declare them as global variables, or by simply referencing them directly if they are in the global scope.
# Example:
global_var = 10

def access_global():
    print("Global variable:", global_var)

access_global()  # Output: Global variable: 10

##Lambda Functions and Higher-Order Functions:

# 1. What are lambda functions in Python, and when are they typically used?
# Lambda functions, also known as anonymous functions, are small, inline functions that are defined using the `lambda` keyword. They are typically used when a simple, one-line function is needed for a short period of time, often as an argument to higher-order functions like `map()`, `filter()`, and `sorted()`.

# 2. Write a Python program that uses lambda functions to sort a list of tuples based on the second element.
# Example:
data = [(1, 5), (3, 2), (2, 8)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(3, 2), (1, 5), (2, 8)]

# 3. Explain the concept of higher-order functions in Python, and provide an example.
# Higher-order functions are functions that can accept other functions as arguments or return functions as results. They enable functional programming paradigms in Python.
# Example:
def apply_function(func, lst):
    return [func(x) for x in lst]

result = apply_function(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(result)  # Output: [1, 4, 9, 16, 25]

# 4. Create a Python function that takes a list of numbers and a function as arguments, applying the function to each element in the list.
def apply_function_to_list(func, lst):
    return [func(x) for x in lst]

result = apply_function_to_list(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(result)  # Output: [1, 4, 9, 16, 25]


##Built-in Functions:
# 1. Describe the role of built-in functions like `len()`, `max()`, and `min()` in Python.
# - `len()`: Returns the number of items in an object, such as a list, tuple, string, etc.
# - `max()`: Returns the largest item in an iterable or the largest of two or more arguments.
# - `min()`: Returns the smallest item in an iterable or the smallest of two or more arguments.
# These built-in functions provide convenient ways to perform common operations on data structures and values.

# 2. Write a Python program that uses the `map()` function to apply a function to each element of a list.
# Example:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# 3. How does the `filter()` function work in Python, and when would you use it?
# The `filter()` function in Python filters elements of an iterable based on a function (predicate) that returns True or False. It returns an iterator containing the elements for which the function returns True.
# You would use `filter()` when you need to selectively extract elements from an iterable based on a condition.
# Example:
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# 4. Create a Python program that uses the `reduce()` function to find the product of all elements in a list.
# Note: Since Python 3, `reduce()` is no longer a built-in function and has been moved to the `functools` module.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

##Function Documentation and Best Practices:
# 1. Explain the purpose of docstrings in Python functions and how to write them.
# Docstrings in Python functions serve as documentation for the function's purpose, usage, parameters, and return values. They provide a convenient way for developers to understand how to use the function without needing to inspect its source code. Docstrings are written as triple quotes (either single or double) immediately after the function definition.

# Example of writing a docstring:
def greet(name):
    """Print a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        None
    """
    print("Hello, " + name)

# 2. Describe some best practices for naming functions and variables in Python, including naming conventions and guidelines.
# - Use descriptive names: Choose names that clearly and accurately describe the purpose or content of the function or variable.
# - Follow naming conventions: Adhere to PEP 8 guidelines for naming conventions, such as using lowercase letters with underscores for function and variable names (snake_case).
# - Use meaningful prefixes or suffixes: Prefixes like `is_` or suffixes like `_list` can provide additional context to the name, making it clearer.
# - Avoid single-letter names (except for iterators): Single-letter names are often ambiguous and should be avoided unless used for simple iterators like `i`, `j`, `k`.
# - Be consistent: Maintain consistency in naming style throughout your codebase for readability and maintainability.
# - Avoid reserved words: Avoid using reserved words or built-in function names as identifiers to prevent conflicts and confusion.

# Example:
# Good function names:
def calculate_area(radius):
    pass

def format_name(first_name, last_name):
    pass

# Good variable names:
total_count = 10
is_valid = True

# These practices contribute to writing clean, readable, and maintainable code in Python.

