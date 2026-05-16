def evaluate_sequence(numbers, operations):
    if len(numbers) < 2:
        return None
    current_list = list(numbers)
    for op in operations:
        if len(current_list) < 2:
            break
        a = current_list.pop(0)
        b = current_list.pop(0)
        result = None
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b != 0:
                result = a / b
            else:
                raise ZeroDivisionError("Division by zero encountered")
        else:
            raise ValueError(f"Unknown operation: {op}")
        current_list.insert(0, result)
    return current_list
if __name__ == '__main__':
    sample_numbers = [10, 5, 2, 8]
    sample_operations = ['+', '-', '*', '/']
    result = evaluate_sequence(sample_numbers, sample_operations)
    print(result)