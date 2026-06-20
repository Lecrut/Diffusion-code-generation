def evaluate_expression(expression_string):
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else float('inf')}
    parts = expression_string.split()
    if len(parts) != 3:
        raise ValueError('Expression must contain exactly two numbers and one operator.')
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        raise ValueError('All parts must be valid numbers.')
    if operator not in operators:
        raise ValueError(f'Invalid operator. Must be one of {list(operators.keys())}.')
    return operators[operator](num1, num2)
if __name__ == '__main__':
    result = evaluate_expression('3 + 5')
    print(result)