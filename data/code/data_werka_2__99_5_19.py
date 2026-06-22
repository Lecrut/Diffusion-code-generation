def calculate_expression(operands, operators):
    if len(operands) < 1:
        raise ValueError('Operands list cannot be empty.')
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    values = list(operands)
    ops = list(operators)
    
    for current_priority in (2, 1):
        i = 0
        while i < len(ops):
            if priority[ops[i]] == current_priority:
                if current_priority == 2:
                    if ops[i] == '/' and values[i + 1] == 0:
                        raise ValueError('Division by zero is not allowed.')
                    left = values.pop(i)
                    right = values.pop(i)
                    if ops[i] == '*':
                        values.insert(i, left * right)
                    else:
                        values.insert(i, left / right)
                else:
                    left = values.pop(i)
                    right = values.pop(i)
                    if ops[i] == '+':
                        values.insert(i, left + right)
                    else:
                        values.insert(i, left - right)
                ops.pop(i)
            else:
                i += 1
                
    return values[0]

if __name__ == '__main__':
    operands = [10, 5, 2, 3]
    operators = ['*', '+', '-']
    result = calculate_expression(operands, operators)
    print(result)
    
    operands2 = [100, 20, 5, 2]
    operators2 = ['/', '/', '-']
    result2 = calculate_expression(operands2, operators2)
    print(result2)