def evaluate_binary_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError('Division by zero')
    elif op == '%':
        if b != 0:
            return a % b
        else:
            raise ValueError('Modulo by zero')
    elif op == '**':
        return a ** b
    else:
        raise ValueError(f'Unsupported operation: {op}')
if __name__ == '__main__':
    print(evaluate_binary_op(10, 5, '+'))
    print(evaluate_binary_op(10, 5, '-'))
    print(evaluate_binary_op(10, 5, '*'))
    print(evaluate_binary_op(10, 5, '/'))
    print(evaluate_binary_op(10, 5, '%'))
    print(evaluate_binary_op(10, 5, '**'))