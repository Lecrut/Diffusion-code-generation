def evaluate_expression(operator, num1, num2):
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else 'Error: Division by zero', '**': lambda x, y: x ** y}
    return operators.get(operator, lambda x, y: 'Invalid operator')(num1, num2)
if __name__ == '__main__':
    result = evaluate_expression('+', 5, 3)
    print(result)
    result = evaluate_expression('/', 10, 0)
    print(result)
    result = evaluate_expression('**', 2, 3)
    print(result)