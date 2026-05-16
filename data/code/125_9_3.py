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
    result_add = calculate('add', num1, num2)
    result_subtract = calculate('subtract', num1, num2)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")