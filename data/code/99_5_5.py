def calculate_expression(operands, operators):
    result = operands[0]
    for operator in operators:
        if operator == '+':
            result += next(operands)
        elif operator == '-':
            result -= next(operands)
        elif operator == '*':
            result *= next(operands)
        elif operator == '/':
            divisor = next(operands)
            if divisor == 0:
                raise ValueError("Division by zero is not allowed.")
            result /= divisor
    return result

if __name__ == '__main__':
    operands = [2, 3, 4, 5]
    operators = ['+', '*', '-']
    print(calculate_expression(operands, operators))