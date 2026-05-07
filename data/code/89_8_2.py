def evaluate_sequence(numbers, operations):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    current_sequence = list(numbers[:])
    for op in operations:
        if len(current_sequence) < 2:
            raise ValueError("Not enough elements to perform operation")
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
            if operand2 == 0:
                raise ZeroDivisionError("Division by zero encountered")
            result = operand1 / operand2
        else:
            raise ValueError(f"Unsupported operation: {op}")
        current_sequence.insert(0, result)
    return current_sequence
if __name__ == '__main__':
    data = [10, 20, 5, 3]
    ops = ['+', '*', '-']
    try:
        result = evaluate_sequence(data, ops)
        print(result)
    except Exception as e:
        print(f"Error: {e}")