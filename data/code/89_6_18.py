def evaluate_binary_operations(operations, numbers):
    result = numbers[0]
    for operation, number in zip(operations, numbers[1:]):
        if operation == '+':
            result += number
        elif operation == '-':
            result -= number
        elif operation == '*':
            result *= number
        elif operation == '/':
            result /= number
        else:
            raise ValueError(f"Invalid operation: {operation}")
    return result

if __name__ == '__main__':
    operations = ['+', '*', '-', '/']
    numbers = [10, 5, 2, 8, 4]
    print(evaluate_binary_operations(operations, numbers))