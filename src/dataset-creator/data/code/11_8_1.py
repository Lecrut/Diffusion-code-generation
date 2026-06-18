import sys
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
if __name__ == '__main__':
    num1 = 15
    num2 = 5
    operator = '*'
    result = calculate(num1, num2, operator)
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    print(f"Operation: {operator}")
    print(f"Result: {result}")