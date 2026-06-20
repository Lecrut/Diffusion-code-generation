OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

def evaluate_expression(op, num1, num2):
    return OPERATIONS.get(op, lambda x, y: "Error: Invalid operator")(num1, num2)

if __name__ == '__main__':
    print(evaluate_expression('+', 10, 5))
    print(evaluate_expression('-', 20, 8))
    print(evaluate_expression('*', 6, 7))