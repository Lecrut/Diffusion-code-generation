def evaluate_operator(op, a, b):
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else 'Error: Division by zero', '**': lambda x, y: x ** y}
    return operators.get(op, 'Invalid operator')(a, b)
if __name__ == '__main__':
    result = evaluate_operator('+', 5, 3)
    print(result)
    result = evaluate_operator('/', 10, 2)
    print(result)
    result = evaluate_operator('**', 2, 3)
    print(result)
    result = evaluate_operator('%', 10, 3)
    print(result)