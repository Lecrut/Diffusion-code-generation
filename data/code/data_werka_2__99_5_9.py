def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if len(operands) == 0:
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
        left_val = values[i + 1]
        if op == '+':
            result = result + left_val
        elif op == '-':
            result = result - left_val
            
    return result

if __name__ == '__main__':
    ops_list = [2, 3, 4, 5, 6]
    op_symbols = ['+', '*', '-', '+']
    print(calculate_expression(ops_list, op_symbols))