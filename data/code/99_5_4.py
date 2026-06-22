def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if len(operands) == 0:
        return 0

    priority = {'*': 2, '/': 2, '+': 1, '-': 1}
    values_stack = [operands[0]]
    operators_stack = []

    for i, op in enumerate(operators):
        current_val = operands[i + 1]
        while (operators_stack and
               priority.get(operators_stack[-1], 0) >= priority.get(op, 0)):
            op2 = operators_stack.pop()
            val2 = values_stack.pop()
            val1 = values_stack.pop()
            if op2 == '+':
                values_stack.append(val1 + val2)
            elif op2 == '-':
                values_stack.append(val1 - val2)
            elif op2 == '*':
                values_stack.append(val1 * val2)
            elif op2 == '/':
                if val2 == 0:
                    raise ValueError('Division by zero is not allowed.')
                values_stack.append(val1 / val2)
        operators_stack.append(op)
        values_stack.append(current_val)

    while operators_stack:
        op2 = operators_stack.pop()
        val2 = values_stack.pop()
        val1 = values_stack.pop()
        if op2 == '+':
            values_stack.append(val1 + val2)
        elif op2 == '-':
            values_stack.append(val1 - val2)
        elif op2 == '*':
            values_stack.append(val1 * val2)
        elif op2 == '/':
            if val2 == 0:
                raise ValueError('Division by zero is not allowed.')
            values_stack.append(val1 / val2)

    return values_stack[0]

if __name__ == '__main__':
    operands = [3, 5, 2, 8, 4]
    operators = ['+', '*', '-', '/']
    result = calculate_expression(operands, operators)
    print(result)