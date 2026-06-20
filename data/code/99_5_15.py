def calculate_expression(operands, operators):
    result = operands[0]
    for operator, operand in zip(operators, operands[1:]):
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    return result

if __name__ == '__main__':
    operands = [2, 3, 4, 5]
    operators = ['+', '*', '-']
    print(calculate_expression(operands, operators))