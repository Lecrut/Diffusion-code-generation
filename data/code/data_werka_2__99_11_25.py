def evaluate_nested_conditions(conditions):
    if not conditions:
        return False
    precedence = {'OR': 1, 'AND': 2, 'NOT': 3}
    output_queue = []
    operator_stack = []
    for token in conditions:
        if token is True or token is False:
            output_queue.append(token)
        elif token in precedence:
            while operator_stack and operator_stack[-1] in precedence and (precedence[operator_stack[-1]] >= precedence[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            raise ValueError(f'Unsupported token: {token}')
    while operator_stack:
        output_queue.append(operator_stack.pop())
    eval_stack = []
    for token in output_queue:
        if token is True or token is False:
            eval_stack.append(token)
        elif token == 'NOT':
            if len(eval_stack) < 1:
                raise ValueError('Insufficient operands for NOT')
            operand = eval_stack.pop()
            eval_stack.append(not operand)
        elif token == 'AND':
            if len(eval_stack) < 2:
                raise ValueError('Insufficient operands for AND')
            right = eval_stack.pop()
            left = eval_stack.pop()
            eval_stack.append(left and right)
        elif token == 'OR':
            if len(eval_stack) < 2:
                raise ValueError('Insufficient operands for OR')
            right = eval_stack.pop()
            left = eval_stack.pop()
            eval_stack.append(left or right)
        else:
            raise ValueError(f'Unsupported token in evaluation: {token}')
    if len(eval_stack) != 1:
        raise ValueError('Invalid expression')
    return eval_stack[0]
if __name__ == '__main__':
    result1 = evaluate_nested_conditions([True, 'AND', False])
    print(result1)
    result2 = evaluate_nested_conditions([True, 'AND', False, 'OR', True])
    print(result2)
    result3 = evaluate_nested_conditions(['NOT', True, 'AND', False])
    print(result3)