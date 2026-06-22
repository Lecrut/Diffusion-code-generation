def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0
    priority = {'*': 2, '/': 2, '+': 1, '-': 1}
    value_stack = [operands[0]]
    op_stack = []
    for i, op in enumerate(operators):
        current_operand = operands[i + 1]
        while op_stack and priority.get(op_stack[-1], 0) >= priority.get(op, 0):
            prev_op = op_stack.pop()
            val_right = value_stack.pop()
            val_left = value_stack.pop()
            if prev_op == '+':
                value_stack.append(val_left + val_right)
            elif prev_op == '-':
                value_stack.append(val_left - val_right)
            elif prev_op == '*':
                value_stack.append(val_left * val_right)
            elif prev_op == '/':
                if val_right == 0:
                    raise ValueError('Division by zero is not allowed.')
                value_stack.append(val_left / val_right)
        op_stack.append(op)
        value_stack.append(current_operand)
    while op_stack:
        remaining_op = op_stack.pop()
        val_right = value_stack.pop()
        val_left = value_stack.pop()
        if remaining_op == '+':
            value_stack.append(val_left + val_right)
        elif remaining_op == '-':
            value_stack.append(val_left - val_right)
        elif remaining_op == '*':
            value_stack.append(val_left * val_right)
        elif remaining_op == '/':
            if val_right == 0:
                raise ValueError('Division by zero is not allowed.')
            value_stack.append(val_left / val_right)
    return value_stack[0]
if __name__ == '__main__':
    sample_operands = [10, 2, 4, 3]
    sample_operators = ['+', '*', '-']
    result = calculate_expression(sample_operands, sample_operators)
    print(result)