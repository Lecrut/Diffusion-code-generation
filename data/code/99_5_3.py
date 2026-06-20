def calculate_expression(operands, operators):
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == '*':
            result *= operands[i + 1]
        elif operators[i] == '+':
            result += operands[i + 1]
        else:
            raise ValueError(f"Unsupported operator: {operators[i]}")
    return result

if __name__ == '__main__':
    print(calculate_expression([2, 3, 4], ['*', '+']))