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
    num1 = 20
    num2 = 5
    operation = '*'
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")