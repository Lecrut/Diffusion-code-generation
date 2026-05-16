def evaluate_binary_op(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        raise ValueError("Invalid operation symbol")
if __name__ == '__main__':
    print(evaluate_binary_op(10, 5, '+'))
    print(evaluate_binary_op(10, 5, '-'))
    print(evaluate_binary_op(10, 5, '*'))
    print(evaluate_binary_op(10, 5, '/'))
    try:
        print(evaluate_binary_op(10, 5, '%'))
    except ValueError as e:
        print(e)