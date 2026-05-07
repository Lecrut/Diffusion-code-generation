def evaluate_binary_op(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
if __name__ == '__main__':
    print(evaluate_binary_op(10, 5, '+'))
    print(evaluate_binary_op(10, 5, '-'))
    print(evaluate_binary_op(10, 5, '*'))
    print(evaluate_binary_op(10, 5, '/'))
    print(evaluate_binary_op(10, 0, '/'))
    print(evaluate_binary_op(10, 5, '%'))