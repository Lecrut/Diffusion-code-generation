def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0
    if not operators:
        return operands[0]
    values = [operands[0]]
    ops = []
    for i, op in enumerate(operators):
        next_val = operands[i + 1]
        if op == '*':
            last_val = values.pop()
            values.append(last_val * next_val)
        elif op == '/':
            last_val = values.pop()
            values.append(last_val / next_val)
        elif op in ('+', '-'):
            values.append(next_val)
            ops.append(op)
        else:
            raise ValueError(f'Unsupported operator: {op}')
    result = values[0]
    for i, op in enumerate(ops):
        next_val = values[i + 1]
        if op == '+':
            result += next_val
        elif op == '-':
            result -= next_val
    return result
if __name__ == '__main__':
    operands = [3, 5, 2, 8, 4]
    operators = ['*', '+', '/', '-']
    result = calculate_expression(operands, operators)
    print(result)