def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Error: Division by zero")
    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def evaluate_expression(op, num1, num2):
    try:
        return operations[op](num1, num2)
    except KeyError:
        raise ValueError("Error: Invalid operator")

if __name__ == '__main__':
    print(evaluate_expression('+', 10, 5))
    print(evaluate_expression('-', 20, 8))
    print(evaluate_expression('*', 6, 7))
    try:
        print(evaluate_expression('/', 10, 0))
    except ValueError as e:
        print(e)