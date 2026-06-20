def evaluate_expression(expression):
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else float('inf')}
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError('Expression must contain exactly two numbers and one operator.')
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        raise ValueError('All parts must be valid numbers.')
    if operator not in operators:
        raise ValueError('Invalid operator. Must be one of +, -, *, /.')
    return operators[operator](num1, num2)
if __name__ == '__main__':
    result = evaluate_expression('10 + 5')
    print(result)