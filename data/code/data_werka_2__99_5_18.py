def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression')
    if not operands:
        return 0
    values = [operands[0]]
    remaining_ops = []
    i = 0
    while i < len(operators):
        op = operators[i]
        if op == '*':
            left = values.pop()
            right = operands[i + 1]
            values.append(left * right)
        elif op == '/':
            left = values.pop()
            right = operands[i + 1]
            if right == 0:
                raise ValueError('Division by zero')
            values.append(left / right)
        else:
            values.append(operands[i + 1])
            remaining_ops.append(op)
        i += 1
    result = values[0]
    for i in range(len(remaining_ops)):
        op = remaining_ops[i]
        next_val = values[i + 1]
        if op == '+':
            result += next_val
        elif op == '-':
            result -= next_val
        else:
            raise ValueError(f'Unsupported operator: {op}')
    return result
if __name__ == '__main__':
    operands = [3, 2, 4, 1, 5]
    operators = ['*', '+', '-', '+']
    result = calculate_expression(operands, operators)
    print(result)