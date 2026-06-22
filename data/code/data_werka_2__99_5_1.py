def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0
    values = [operands[0]]
    ops = []
    for i, op in enumerate(operators):
        if op == '*':
            values[-1] = values[-1] * operands[i + 1]
        elif op == '/':
            if operands[i + 1] == 0:
                raise ValueError('Division by zero is not allowed.')
            values[-1] = values[-1] / operands[i + 1]
        else:
            ops.append(op)
            values.append(operands[i + 1])
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
    operands = [3, 2, 4, 5, 1]
    operators = ['+', '*', '-', '+']
    result = calculate_expression(operands, operators)
    print(result)