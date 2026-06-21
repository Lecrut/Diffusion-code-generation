def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0
    values = []
    ops = []
    current_value = operands[0]
    for i, op in enumerate(operators):
        next_operand = operands[i + 1]
        if op == '*':
            current_value *= next_operand
        elif op == '/':
            if next_operand == 0:
                raise ValueError('Division by zero.')
            current_value /= next_operand
        else:
            values.append(current_value)
            ops.append(op)
            current_value = next_operand
    values.append(current_value)
    result = values[0]
    for i, op in enumerate(ops):
        next_value = values[i + 1]
        if op == '+':
            result += next_value
        elif op == '-':
            result -= next_value
        else:
            raise ValueError(f'Unsupported operator: {op}')
    return result
if __name__ == '__main__':
    operands = [3, 2, 4, 5, 1]
    operators = ['*', '+', '/', '-']
    result = calculate_expression(operands, operators)
    print(result)