OPERATIONS = {
    '+': lambda num1, num2: num1 + num2,
    '-': lambda num1, num2: num1 - num2,
    '*': lambda num1, num2: num1 * num2,
    '/': lambda num1, num2: (num1 / num2) if num2 != 0 else "Error: Division by zero"
}

def evaluate_expression(op, num1, num2):
    return OPERATIONS.get(op, lambda _, __: "Error: Invalid operator")(num1, num2)

if __name__ == '__main__':
    print(evaluate_expression('+', 10, 5))
    print(evaluate_expression('-', 20, 8))
    print(evaluate_expression('*', 6, 7))
    print(evaluate_expression('/', 9, 3))
    print(evaluate_expression('/', 9, 0))
    print(evaluate_expression('^', 2, 3))