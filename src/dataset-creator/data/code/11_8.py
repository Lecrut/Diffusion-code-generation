import sys
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
if __name__ == '__main__':
    num1 = 15
    num2 = 5
    operation = '*'
    result = calculate(num1, num2, operation)
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    print(f"Operation: {operation}")
    print(f"Result: {result}")