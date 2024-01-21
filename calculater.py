num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = input("Enter the operator (+, *, /, -): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero.")
        result = None
else:
    print("Error: Invalid operator.")
    result = None

if result is not None:
    print("Result:", result)
