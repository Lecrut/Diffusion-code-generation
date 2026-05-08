def calculate_expression(operands, operators):
    if not operands:
        return None
    if len(operands) != len(operators) + 1:
        raise ValueError("Operands and operators lists must have lengths differing by exactly one.")
    result = list(operands)
    i = 0
    while i < len(operators):
        operator = operators[i]
        operand1 = result[i]
        operand2 = result[i+1]
        if operator == '+':
            result[i] = operand1 + operand2
            result.pop(i+1)
        elif operator == '-':
            result[i] = operand1 - operand2
            result.pop(i+1)
        elif operator == '*':
            result[i] = operand1 * operand2
            result.pop(i+1)
        elif operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError("Division by zero encountered.")
            result[i] = operand1 / operand2
            result.pop(i+1)
        else:
            raise ValueError(f"Unknown operator: {operator}")
        i = 0                                                                   
    return result[0]
if __name__ == '__main__':
    operands1 = [3, 4, 2]
    operators1 = ['+', '*']
    print(f"Operands: {operands1}, Operators: {operators1}")
    try:
        result1 = calculate_expression(operands1, operators1)
        print(f"Result: {result1}")
    except Exception as e:
        print(f"Error: {e}")
    operands2 = [10, 5, 2, 3]
    operators2 = ['-', '+', '*', '/']
    print(f"\nOperands: {operands2}, Operators: {operators2}")
    try:
        result2 = calculate_expression(operands2, operators2)
        print(f"Result: {result2}")
    except Exception as e:
        print(f"Error: {e}")
    operands3 = [10, 20, 30]
    operators3 = ['+', '+']
    print(f"\nOperands: {operands3}, Operators: {operators3}")
    try:
        result3 = calculate_expression(operands3, operators3)
        print(f"Result: {result3}")
    except Exception as e:
        print(f"Error: {e}")