def evaluate_binary_op(a, b, op):
    operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else float('inf')}
    result = operations.get(op)
    if result is None:
        raise ValueError(f'Unsupported operation: {op}')
    return result(a, b)
if __name__ == '__main__':
    num1 = 10.0
    num2 = 3.0
    try:
        print(evaluate_binary_op(num1, num2, '+'))
        print(evaluate_binary_op(num1, num2, '-'))
        print(evaluate_binary_op(num1, num2, '*'))
        print(evaluate_binary_op(num1, num2, '/'))
        print(evaluate_binary_op(num1, 0, '/'))
    except ValueError as e:
        print(e)