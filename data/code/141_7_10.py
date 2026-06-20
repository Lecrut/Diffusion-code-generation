def evaluate_expression(expr):

    def apply_operator(op, stack):
        right = stack.pop()
        left = stack.pop()
        if op == 'AND':
            stack.append(left and right)
        elif op == 'OR':
            stack.append(left or right)
        elif op == 'NOT':
            stack.append(not right)
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    operators = set(precedence.keys())
    tokens = expr.split()
    stack_values = []
    stack_ops = []
    for token in tokens:
        if token.isdigit():
            stack_values.append(int(token))
        elif token in operators:
            while stack_ops and stack_ops[-1] != '(' and (precedence[stack_ops[-1]] >= precedence[token]):
                apply_operator(stack_ops.pop(), stack_values)
            stack_ops.append(token)
        elif token == '(':
            stack_ops.append(token)
        elif token == ')':
            while stack_ops[-1] != '(':
                apply_operator(stack_ops.pop(), stack_values)
            stack_ops.pop()
    while stack_ops:
        apply_operator(stack_ops.pop(), stack_values)
    return stack_values[0]
if __name__ == '__main__':
    expression = '3 AND (5 OR NOT 2)'
    result = evaluate_expression(expression)
    print(result)