def calculate(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    else:
        raise ValueError("Invalid operation")
if __name__ == '__main__':
    num1 = 10
    num2 = 4
    op1 = 'add'
    result1 = calculate(op1, num1, num2)
    print(f"Addition of {num1} and {num2}: {result1}")
    num3 = 10
    num4 = 4
    op2 = 'subtract'
    result2 = calculate(op2, num3, num4)
    print(f"Subtraction of {num3} and {num4}: {result2}")