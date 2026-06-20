def calculate_expression(operands, operators):
    operator_map = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y if y != 0 else float('inf')}
    
    result = operands[0]
    for i in range(len(operators)):
        result = operator_map[operators[i]](result, operands[i + 1])
    return result

if __name__ == '__main__':
    operands = [2, 3, 4, 5]
    operators = ['+', '*', '-']
    print(calculate_expression(operands, operators))