def calculate_expression(operands, operators):
    if len(operands) != len(operators) + 1:
        raise ValueError('Operands and operators must form a valid expression sequence.')
    if not operands:
        return 0

    priority = {'*': 2, '/': 2, '+': 1, '-': 1}
    values_stack = [operands[0]]
    ops_stack = []

    def apply_op(v1, v2, op):
        if op == '+':
            return v1 + v2
        if op == '-':
            return v1 - v2
        if op == '*':
            return v1 * v2
        if op == '/':
            if v2 == 0:
                raise ValueError('Division by zero is not allowed.')
            return v1 / v2
        return v2

    def process_higher_or_equal(new_op):
        while ops_stack and priority.get(ops_stack[-1], 0) >= priority.get(new_op, 0):
            op = ops_stack.pop()
            v2 = values_stack.pop()
            v1 = values_stack.pop()
            result = apply_op(v1, v2, op)
            values_stack.append(result)

    for i, op in enumerate(operators):
        current_val = operands[i + 1]
        process_higher_or_equal(op)
        ops_stack.append(op)
        values_stack.append(current_val)

    while ops_stack:
        op = ops_stack.pop()
        v2 = values_stack.pop()
        v1 = values_stack.pop()
        result = apply_op(v1, v2, op)
        values_stack.append(result)

    return values_stack[0]

if __name__ == '__main__':
    nums = [3, 2, 4, 5, 1]
    ops = ['+', '*', '-', '/']
    final_result = calculate_expression(nums, ops)
    print(final_result)