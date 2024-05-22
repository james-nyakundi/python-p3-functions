#!/usr/bin/env python3

def greet_programmer():
    print("Hello,programmer!")
    greet_programmer()
    pass

def greet(name):
  print("Hello, {}!".format(name))

# You can call the function like this:
greet("Naureen")
pass
def greet_with_default(name="programmer"):
    print("Hello, {}!".format(name))

# Call the function with no arguments
greet_with_default()

# Call the function with one argument
greet_with_default("Sunny")

pass

def add(num1, num2):
    
    return num1 + num2

# Call the function with two arguments and print the return value
sum_result = add(1, 2)
print(sum_result)

pass

def halve(number):
    
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2

# Test cases
result1 = halve(4)
print(result1)  # Output: 2

result2 = halve("two")
print(result2)  # Output: None

pass
