#!/usr/bin/env python3
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 / num2
quotient = num1 * num2

print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} / {num2} = {product :.0f}")
print(f"{num1} * {num2} = {quotient}")