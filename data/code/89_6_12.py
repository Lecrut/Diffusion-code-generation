def evaluate_binary_operations(operations, numbers):
    result = numbers[0]
    for operation, number in zip(operations, numbers[1:]):
        if operation == 'add':
            result += number
        elif operation == 'sub':
            result -= number
        elif operation == 'mul':
            result *= number
        elif operation == 'div':
            result /= number
    return result

if __name__ == '__main__':
    operations = ['add', 'mul', 'div']
    numbers = [10, 5, 2, 4]
    print(evaluate_binary_operations(operations, numbers))