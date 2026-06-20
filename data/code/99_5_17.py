def evaluate_expression(operands, operators):
    if len(operators) != len(operands) - 1:
        raise ValueError("Mismatch between number of operands and operators.")
    
    result = operands[0]
    i = 0
    while i < len(operators):
        op = operators[i]
        next_operand = operands[i + 1]
        
        if op == '+':
            result += next_operand
        elif op == '-':
            result -= next_operand
        elif op == '*':
            result *= next_operand
        elif op == '/':
            if next_operand == 0:
                raise ValueError("Division by zero is not allowed.")
            result /= next_operand
        else:
            raise ValueError(f"Unsupported operator: {op}")
        
        i += 1
    
    return result

if __name__ == '__main__':
    operands = [5, 2, 8, 3]
    operators = ['+', '*', '/']
    print(evaluate_expression(operands, operators))