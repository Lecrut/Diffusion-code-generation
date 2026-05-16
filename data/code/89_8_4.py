def evaluate_sequence(numbers, operations):
    if len(numbers) < 2:
        return None
    current_list = list(numbers)
    for op in operations:
        if len(current_list) < 2:
            break
        operand1 = current_list.pop(0)
        operand2 = current_list.pop(0)
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
        current_list.insert(0, result)
    return current_list
if __name__ == '__main__':
    data = [10, 20, 5, 3]
    ops = ['+', '-', '*']
    result = evaluate_sequence(data, ops)
    print(result)