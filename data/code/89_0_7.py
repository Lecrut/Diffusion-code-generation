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
            raise ValueError('Cannot divide by zero')
    else:
        raise ValueError('Unsupported operation')
if __name__ == '__main__':
    print(evaluate_binary_op(10, 5, '+'))
    print(evaluate_binary_op(10, 5, '-'))
    print(evaluate_binary_op(10, 5, '*'))
    print(evaluate_binary_op(10, 5, '/'))