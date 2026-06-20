def evaluate_binary_op(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {op}")

if __name__ == '__main__':
    num1 = 10.0
    num2 = 3.0
    try:
        result_add = evaluate_binary_op(num1, num2, 'add')
        print(f"Addition: {result_add}")
        
        result_sub = evaluate_binary_op(num1, num2, 'sub')
        print(f"Subtraction: {result_sub}")
        
        result_mul = evaluate_binary_op(num1, num2, 'mul')
        print(f"Multiplication: {result_mul}")
        
        result_div = evaluate_binary_op(num1, num2, 'div')
        print(f"Division: {result_div}")
    except ValueError as e:
        print(e)