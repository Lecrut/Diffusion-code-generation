def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0
    values = [operands[0]]
    ops = []
    for i, op in enumerate(operators):
        right_val = operands[i + 1]
        if op == '*':
            values[-1] = values[-1] * right_val
        elif op == '/':
            if right_val == 0:
                raise ValueError('Division by zero is not allowed.')
            values[-1] = values[-1] / right_val
        else:
            ops.append(op)
            values.append(right_val)
    result = values[0]
    for i, op in enumerate(ops):
        if op == '+':
            result = result + values[i + 1]
        elif op == '-':
            result = result - values[i + 1]
        else:
            raise ValueError(f'Unsupported operator: {op}')
    return result
if __name__ == '__main__':
    operands = [3, 2, 8, 4, 1]
    operators = ['*', '+', '/', '-']
    result = calculate_expression(operands, operators)
    print(result)