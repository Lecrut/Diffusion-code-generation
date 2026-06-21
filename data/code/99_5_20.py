def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0
    current_term = operands[0]
    terms = []
    remaining_ops = []
    for i, op in enumerate(operators):
        next_val = operands[i + 1]
        if op == '*':
            current_term *= next_val
        elif op == '/':
            if next_val == 0:
                raise ValueError('Division by zero.')
            current_term /= next_val
        else:
            terms.append(current_term)
            remaining_ops.append(op)
            current_term = next_val
    terms.append(current_term)
    result = terms[0]
    for i, op in enumerate(remaining_ops):
        next_val = terms[i + 1]
        if op == '+':
            result += next_val
        elif op == '-':
            result -= next_val
        else:
            raise ValueError(f'Unsupported operator: {op}')
    return result
if __name__ == '__main__':
    operands = [3, 2, 8, 1, 5]
    operators = ['*', '+', '/', '-']
    result = calculate_expression(operands, operators)
    print(result)