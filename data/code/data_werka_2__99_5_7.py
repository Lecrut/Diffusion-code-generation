def calculate_expression(operands, operators):
    MULTIPLY_DIVIDE_PRIORITY = 2
    ADD_SUBTRACT_PRIORITY = 1
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if len(operands) == 0:
        return 0
    
    values = []
    ops = []
    
    values.append(operands[0])
    
    for i, op in enumerate(operators):
        next_val = operands[i + 1]
        current_priority = MULTIPLY_DIVIDE_PRIORITY if op in ('*', '/') else ADD_SUBTRACT_PRIORITY
        
        while ops and MULTIPLY_DIVIDE_PRIORITY >= current_priority:
            top_op = ops.pop()
            right = values.pop()
            left = values.pop()
            
            if top_op == '+':
                values.append(left + right)
            elif top_op == '-':
                values.append(left - right)
            elif top_op == '*':
                values.append(left * right)
            elif top_op == '/':
                if right == 0:
                    raise ValueError('Division by zero is not allowed.')
                values.append(left / right)
            else:
                raise ValueError('Unsupported operator.')
        
        ops.append(op)
        values.append(next_val)
        
    while ops:
        top_op = ops.pop()
        right = values.pop()
        left = values.pop()
        
        if top_op == '+':
            values.append(left + right)
        elif top_op == '-':
            values.append(left - right)
        elif top_op == '*':
            values.append(left * right)
        elif top_op == '/':
            if right == 0:
                raise ValueError('Division by zero is not allowed.')
            values.append(left / right)
        else:
            raise ValueError('Unsupported operator.')
            
    return values[0]

if __name__ == '__main__':
    sample_operands = [3, 5, 2, 8, 4]
    sample_operators = ['+', '*', '-', '/']
    result = calculate_expression(sample_operands, sample_operators)
    print(result)