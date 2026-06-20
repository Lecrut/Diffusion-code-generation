def evaluate_binary_op(num1, num2, operation):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: (x / y) if y != 0 else "Error: Division by zero"
    }
    return operations.get(operation, lambda x, y: "Error: Invalid operation")(num1, num2)

if __name__ == '__main__':
    a = 10
    b = 5
    print(evaluate_binary_op(a, b, '+'))
    print(evaluate_binary_op(a, b, '-'))
    print(evaluate_binary_op(a, b, '*'))
    print(evaluate_binary_op(a, b, '/'))
    print(evaluate_binary_op(a, 0, '/'))
    print(evaluate_binary_op(a, b, '^'))