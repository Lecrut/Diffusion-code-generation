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
    result_add = evaluate_binary_op(10, 5, '+')
    result_sub = evaluate_binary_op(10, 5, '-')
    result_mul = evaluate_binary_op(10, 5, '*')
    result_div = evaluate_binary_op(10, 5, '/')
    
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")
    print(f"Multiplication: {result_mul}")
    print(f"Division: {result_div}")