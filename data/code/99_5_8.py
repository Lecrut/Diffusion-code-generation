OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else float('inf')
}

def calculate_expression(operands, operators):
    result = operands[0]
    for i in range(len(operators)):
        operator = operators[i]
        next_operand = operands[i + 1]
        result = OPERATORS[operator](result, next_operand)
    return result

if __name__ == '__main__':
    operands = [2, 3, 4, 5]
    operators = ['+', '*', '-']
    print(calculate_expression(operands, operators))