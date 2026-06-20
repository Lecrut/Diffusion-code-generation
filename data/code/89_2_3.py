def evaluate_expression(expression):
    operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else float('inf')}
    tokens = expression.split()
    if len(tokens) != 3:
        raise ValueError('Invalid input format')
    num1, operator, num2 = tokens
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError('Both operands must be numbers')
    if operator not in operations:
        raise ValueError('Unsupported operator')
    return operations[operator](num1, num2)
if __name__ == '__main__':
    try:
        result = evaluate_expression('10 / 2')
        print(result)
    except ValueError as e:
        print(e)