def calculate_expression(operands, operators):
    result = operands[0]
    i = 0
    while i < len(operators):
        if operators[i] == '+':
            result += operands[i + 1]
        elif operators[i] == '-':
            result -= operands[i + 1]
        elif operators[i] == '*':
            result *= operands[i + 1]
        elif operators[i] == '/':
            if operands[i + 1] == 0:
                raise ValueError("Division by zero is not allowed.")
            result /= operands[i + 1]
        else:
            raise ValueError(f"Unsupported operator: {operators[i]}")
        i += 1
    return result

if __name__ == '__main__':
    operands = [2, 3, 4, 5]
    operators = ['+', '*', '-']
    print(calculate_expression(operands, operators))