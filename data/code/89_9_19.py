def evaluate_binary_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError('Division by zero')
        return a / b
    else:
        raise ValueError('Unsupported operation')
if __name__ == '__main__':
    print(evaluate_binary_op(10, 5, '+'))
    print(evaluate_binary_op(10, 5, '-'))
    print(evaluate_binary_op(10, 5, '*'))
    try:
        print(evaluate_binary_op(10, 0, '/'))
    except ValueError as e:
        print(e)
    try:
        print(evaluate_binary_op(10, 5, '%'))
    except ValueError as e:
        print(e)