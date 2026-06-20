def evaluate_binary_op(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            raise ValueError("Error: Division by zero")
    else:
        raise ValueError("Error: Invalid operation")

if __name__ == '__main__':
    a = 10
    b = 5
    print(evaluate_binary_op(a, b, '+'))
    print(evaluate_binary_op(a, b, '-'))
    print(evaluate_binary_op(a, b, '*'))
    print(evaluate_binary_op(a, b, '/'))
    try:
        print(evaluate_binary_op(a, 0, '/'))
    except ValueError as e:
        print(e)
    try:
        print(evaluate_binary_op(a, b, '%'))
    except ValueError as e:
        print(e)