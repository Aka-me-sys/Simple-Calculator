print("Simple Calculator")

num1 = float(input("Enter your first number"))
num2 = float(input("Enter you second number"))

question = input("What do you want to do + - / * ")

if question == "+":
    result = num1 + num2
elif question == "-":
    result = num1 - num2
elif question == "/":
    result = num1 / num2
elif question == "*":
    result = num1 * num2 
else:
    print("No operation like that")

print("Result", result)