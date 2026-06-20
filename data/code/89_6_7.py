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
            raise ValueError(f"Unsupported operation: {operation}")
    return result

if __name__ == '__main__':
    operations = ['+', '*', '-']
    numbers = [2, 3, 4, 5]
    print(evaluate_binary_operations(operations, numbers))