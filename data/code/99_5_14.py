def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0
    reduced_operands = []
    reduced_operators = []
    current_operand = operands[0]
    for i, op in enumerate(operators):
        next_operand = operands[i + 1]
        if op == '*':
            current_operand = current_operand * next_operand
        elif op == '/':
            if next_operand == 0:
                raise ValueError('Division by zero is not allowed.')
            current_operand = current_operand / next_operand
        else:
            reduced_operands.append(current_operand)
            reduced_operators.append(op)
            current_operand = next_operand
    reduced_operands.append(current_operand)
    result = reduced_operands[0]
    for i, op in enumerate(reduced_operators):
        next_operand = reduced_operands[i + 1]
        if op == '+':
            result = result + next_operand
        elif op == '-':
            result = result - next_operand
        else:
            raise ValueError(f'Unsupported operator: {op}')
    return result
if __name__ == '__main__':
    operands = [3, 2, 4, 5, 1]
    operators = ['*', '+', '-', '+']
    result = calculate_expression(operands, operators)
    print(result)