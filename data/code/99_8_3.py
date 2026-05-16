def calculate_expression(operands, operators):
    if not operands:
        return None
    result = operands[0]
    current_operator_index = 0
    for i in range(len(operators)):
        operator = operators[i]
        operand = operands[i + 1]
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            if operand == 0:
                raise ZeroDivisionError("Division by zero")
            result /= operand
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    return result
if __name__ == '__main__':
    operands1 = [5, 3, 2]
    operators1 = ['+', '*']
    print(f"Operands: {operands1}, Operators: {operators1}")
    try:
        result1 = calculate_expression(operands1, operators1)
        print(f"Result: {result1}")
    except Exception as e:
        print(f"Error: {e}")
    operands2 = [10, 4, 2]
    operators2 = ['-', '+', '*']
    print(f"\nOperands: {operands2}, Operators: {operators2}")
    try:
        result2 = calculate_expression(operands2, operators2)
        print(f"Result: {result2}")
    except Exception as e:
        print(f"Error: {e}")
    operands3 = [20, 5, 2, 3]
    operators3 = ['*', '/', '+']
    print(f"\nOperands: {operands3}, Operators: {operators3}")
    try:
        result3 = calculate_expression(operands3, operators3)
        print(f"Result: {result3}")
    except Exception as e:
        print(f"Error: {e}")