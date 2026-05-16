def evaluate_sequence(numbers, operations):
    if len(numbers) < 2:
        return None
    current_sequence = list(numbers[:2])
    for op in operations:
        if len(current_sequence) < 2:
            break
        a = current_sequence.pop(0)
        b = current_sequence.pop(0)
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
            raise ValueError(f"Unsupported operation: {op}")
        current_sequence.insert(0, result)
    return current_sequence
if __name__ == '__main__':
    data = [10, 5, 2, 8]
    ops = ['+', '-', '*', '/']
    result = evaluate_sequence(data, ops)
    if result is not None:
        print(result)