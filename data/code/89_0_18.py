def is_valid_operation(operation):
    return operation in ['+', '-', '*', '/']

def evaluate_binary_op(num1, num2, operation):
    if not is_valid_operation(operation):
        raise ValueError("Invalid operation")
    
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    else:
        if num2 == 0:
            raise ValueError("Error: Division by zero")
        return num1 / num2

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