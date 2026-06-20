def calculate_expression(operands, operators):
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += operands[i + 1]
        elif operators[i] == '-':
            result -= operands[i + 1]
        elif operators[i] == '*':
            result *= operands[i + 1]
        elif operators[i] == '/':
            result /= operands[i + 1]
    return result

if __name__ == '__main__':
    sample_operands = [2, 3, 4, 5]
    sample_operators = ['+', '*', '-']
    print(calculate_expression(sample_operands, sample_operators))