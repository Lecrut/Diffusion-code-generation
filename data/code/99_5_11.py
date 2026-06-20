def validate_operands(operands):
    if not all(isinstance(op, (int, float)) for op in operands):
        raise ValueError("All operands must be numbers")

def validate_operators(operators):
    if not all(operator in ('+', '-', '*', '/') for operator in operators):
        raise ValueError("Unsupported operator encountered")

def calculate_expression(operands, operators):
    validate_operands(operands)
    validate_operators(operators)
    
    result = operands[0]
    index = 1
    i = 0
    
    while index < len(operators) and i < len(operators):
        operator = operators[i]
        next_operand = operands[index]
        
        if operator == '+':
            result += next_operand
        elif operator == '-':
            result -= next_operand
        elif operator == '*':
            result *= next_operand
        elif operator == '/':
            if next_operand == 0:
                raise ValueError("Division by zero is not allowed.")
            result /= next_operand
        
        index += 1
        i += 1
    
    return result

if __name__ == '__main__':
    operands = [2, 3, 4, 5]
    operators = ['+', '*', '-']
    print(calculate_expression(operands, operators))