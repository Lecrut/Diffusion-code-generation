from operator import add, sub, mul, truediv

def calculate_expression(operands, operators):
    if not operands:
        return 0
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    
    def _get_op(char):
        if char == '+':
            return add
        if char == '-':
            return sub
        if char == '*':
            return mul
        if char == '/':
            return truediv
        raise ValueError(f'Unsupported operator: {char}')

    result = operands[0]
    index = 0
    length = len(operators)

    while index < length:
        op_char = operators[index]
        if op_char in ('*', '/'):
            right = operands[index + 1]
            if op_char == '/' and right == 0:
                raise ValueError('Division by zero is not allowed.')
            result = _get_op(op_char)(result, right)
            if index + 1 < length and operators[index + 1] in ('*', '/'):
                index += 1
                continue
            index += 1
            if index < length:
                result = operands[index]
                index += 1
            else:
                break
        else:
            index += 1
            if index < length:
                op_char = operators[index]
                right = operands[index + 1]
                result = _get_op(op_char)(result, right)
                index += 1

    return result

if __name__ == '__main__':
    op_list = [2, 3, 4, 5]
    operator_list = ['+', '*', '-', '+']
    calc_result = calculate_expression(op_list, operator_list)
    print(calc_result)