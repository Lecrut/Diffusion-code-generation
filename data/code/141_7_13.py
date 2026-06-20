def evaluate_expression(expr):
    operators = {'AND': lambda x, y: x and y, 'OR': lambda x, y: x or y, 'NOT': lambda x: not x}
    tokens = expr.split()
    stack = []
    for token in tokens:
        if token in operators:
            right = stack.pop()
            left = stack.pop()
            result = operators[token](left, right)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]
if __name__ == '__main__':
    expression = '3 AND 5 OR NOT 2'
    result = evaluate_expression(expression)
    print(result)