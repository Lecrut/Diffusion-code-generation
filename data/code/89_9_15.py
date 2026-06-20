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
            raise ValueError("Division by zero is not allowed.")
    else:
        raise ValueError(f"Unsupported operation: {op}")

if __name__ == '__main__':
    num1 = 10.0
    num2 = 3.0
    try:
        result_add = evaluate_binary_op(num1, num2, '+')
        result_sub = evaluate_binary_op(num1, num2, '-')
        result_mul = evaluate_binary_op(num1, num2, '*')
        result_div = evaluate_binary_op(num1, num2, '/')
        print(f"Number 1: {num1}")
        print(f"Number 2: {num2}")
        print("-" * 30)
        print(f"Addition (a + b): {result_add}")
        print(f"Subtraction (a - b): {result_sub}")
        print(f"Multiplication (a * b): {result_mul}")
        print(f"Division (a / b): {result_div}")
    except ValueError as e:
        print(e)