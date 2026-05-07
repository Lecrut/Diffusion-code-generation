def evaluate_sequence(numbers, operations):
    if len(numbers) < 2:
        return []
    current_sequence = list(numbers[:2])
    for op in operations:
        if len(current_sequence) < 2:
            break
        operand2 = current_sequence.pop(1)
        operand1 = current_sequence.pop(0)
        result = None
        if op == '+':
            result = operand1 + operand2
        elif op == '-':
            result = operand1 - operand2
        elif op == '*':
            result = operand1 * operand2
        elif op == '/':
            if operand2 != 0:
                result = operand1 / operand2
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
    print(result)