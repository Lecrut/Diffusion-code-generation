def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0
    nums = list(operands)
    ops = list(operators)
    i = 0
    while i < len(ops):
        op = ops[i]
        if op == '*':
            nums[i] = nums[i] * nums[i + 1]
            nums.pop(i + 1)
            ops.pop(i)
        elif op == '/':
            if nums[i + 1] == 0:
                raise ValueError('Division by zero.')
            nums[i] = nums[i] / nums[i + 1]
            nums.pop(i + 1)
            ops.pop(i)
        else:
            i += 1
    result = nums[0]
    for i in range(len(ops)):
        op = ops[i]
        if op == '+':
            result += nums[i + 1]
        elif op == '-':
            result -= nums[i + 1]
        else:
            raise ValueError(f'Unsupported operator: {op}')
    return result
if __name__ == '__main__':
    operands = [3, 5, 2, 8, 4]
    operators = ['+', '*', '-', '/']
    result = calculate_expression(operands, operators)
    print(result)