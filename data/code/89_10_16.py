def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    else:
        return num1 / num2

operation_map = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def evaluate_expression(op, num1, num2):
    return operation_map[op](num1, num2)

if __name__ == '__main__':
    print(evaluate_expression('+', 10, 5))
    print(evaluate_expression('-', 20, 8))
    print(evaluate_expression('*', 6, 7))
    print(evaluate_expression('/', 15, 3))