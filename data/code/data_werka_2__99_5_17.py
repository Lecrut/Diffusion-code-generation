def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence')
    if not operands:
        return 0
    if len(operands) == 1:
        return operands[0]
    new_operands = [operands[0]]
    new_operators = []
    for i, op in enumerate(operators):
        right_operand = operands[i + 1]
        if op == '*':
            new_operands[-1] = new_operands[-1] * right_operand
        elif op == '/':
            if right_operand == 0:
                raise ValueError('Division by zero')
            new_operands[-1] = new_operands[-1] / right_operand
        elif op == '+':
            new_operands.append(right_operand)
            new_operators.append('+')
        elif op == '-':
            new_operands.append(right_operand)
            new_operators.append('-')
        else:
            raise ValueError(f'Unsupported operator: {op}')
    result = new_operands[0]
    for i, op in enumerate(new_operators):
        right_operand = new_operands[i + 1]
        if op == '+':
            result = result + right_operand
        elif op == '-':
            result = result - right_operand
    return result
if __name__ == '__main__':
    operands = [3, 2, 4, 5, 1]
    operators = ['*', '+', '-', '+']
    result = calculate_expression(operands, operators)
    print(result)