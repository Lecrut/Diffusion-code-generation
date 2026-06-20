def evaluate_binary_op(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is not allowed.")
    else:
        raise ValueError(f"Unsupported operation: {op}")

if __name__ == '__main__':
    num1 = 10.0
    num2 = 3.0
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print("-" * 30)
    print(f"Addition (a + b): {evaluate_binary_op(num1, num2, 'add')}")
    print(f"Subtraction (a - b): {evaluate_binary_op(num1, num2, 'sub')}")
    print(f"Multiplication (a * b): {evaluate_binary_op(num1, num2, 'mul')}")
    print(f"Division (a / b): {evaluate_binary_op(num1, num2, 'div')}")