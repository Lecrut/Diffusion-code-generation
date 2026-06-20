def evaluate_expression(expression):
    operators = {'AND': lambda x, y: x and y, 'OR': lambda x, y: x or y, 'NOT': lambda x: not x}

    def is_operator(token):
        return token in operators

    def apply_operator(op, stack):
        right = stack.pop()
        if op == 'NOT':
            stack.append(operators[op](right))
        else:
            left = stack.pop()
            stack.append(operators[op](left, right))

    def precedence(op):
        return 1 if op == 'NOT' else 2
    tokens = expression.split()
    stack = []
    operator_stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif is_operator(token):
            while operator_stack and precedence(operator_stack[-1]) >= precedence(token):
                apply_operator(operator_stack.pop(), stack)
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                apply_operator(operator_stack.pop(), stack)
            operator_stack.pop()
    while operator_stack:
        apply_operator(operator_stack.pop(), stack)
    return stack[0]
if __name__ == '__main__':
    expression = 'NOT 3 OR (5 AND 2)'
    result = evaluate_expression(expression)
    print(result)