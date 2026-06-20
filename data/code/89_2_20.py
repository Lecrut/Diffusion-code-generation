def evaluate_expression(expression):
    tokens = expression.split()
    if len(tokens) != 3:
        raise ValueError("Invalid input format")
    
    try:
        num1, operator, num2 = float(tokens[0]), tokens[1], float(tokens[2])
    except ValueError:
        raise ValueError("Both operands must be numbers")

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf')
    }

    if operator not in operations:
        raise ValueError("Unsupported operator")

    return operations[operator](num1, num2)

if __name__ == '__main__':
    try:
        result = evaluate_expression('10 / 2')
        print(result)
    except Exception as e:
        print(e)