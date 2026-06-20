def calculate_expression(operands, operators):
    result = operands[0]
    i = 1
    while i < len(operators):
        if operators[i] == '*':
            result *= operands[i + 1]
            i += 2
        elif operators[i] == '/':
            if operands[i + 1] == 0:
                raise ValueError("Division by zero is not allowed.")
            result /= operands[i + 1]
            i += 2
        else:
            break
    
    for j in range(i, len(operators)):
        if operators[j] == '+':
            result += operands[j + 1]
        elif operators[j] == '-':
            result -= operands[j + 1]
    
    return result

if __name__ == '__main__':
    print(calculate_expression([2, 3, 4, 5], ['+', '*', '-']))