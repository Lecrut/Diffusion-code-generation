def evaluate_binary_operations(operations, numbers):
    result = numbers[0]
    for op, num in zip(operations, numbers[1:]):
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            result /= num
        else:
            raise ValueError(f"Unsupported operation: {op}")
    return result

if __name__ == '__main__':
    operations = ['+', '*', '-', '/']
    numbers = [10, 5, 3, 2, 4]
    print(evaluate_binary_operations(operations, numbers))