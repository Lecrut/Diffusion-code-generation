def evaluate_expression(operands, operators):
    if len(operators) != len(operands) - 1:
        raise ValueError("The number of operators must be one less than the number of operands.")
    
    def apply_operator(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ValueError("Division by zero is not allowed.")
            return a / b
        else:
            raise ValueError(f"Unsupported operator: {op}")
    
    result = operands[0]
    for i, op in enumerate(operators):
        result = apply_operator(op, result, operands[i + 1])
    
    return result

if __name__ == '__main__':
    operands = [2, 3, 4, 5]
    operators = ['+', '*', '-']
    print(evaluate_expression(operands, operators))