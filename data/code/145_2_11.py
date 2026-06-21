def evaluate_nested(expression):
    if isinstance(expression, str):
        expression = expression.replace('and', '&&').replace('or', '||').replace('not', '!')
    tokens = expression.split()
    if not tokens:
        return False
    result_stack = []
    operator_stack = []
    
    def apply_op():
        op = operator_stack.pop()
        if op == 'NOT':
            operand = result_stack.pop()
            result_stack.append(not operand)
        elif op == 'AND':
            right = result_stack.pop()
            left = result_stack.pop()
            result_stack.append(left and right)
        elif op == 'OR':
            right = result_stack.pop()
            left = result_stack.pop()
            result_stack.append(left or right)

    for token in tokens:
        if token in ('True', 'False'):
            result_stack.append(token == 'True')
        elif token == '(':
            operator_stack.append('(')
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                apply_op()
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        else:
            operator_stack.append(token)

    while operator_stack:
        apply_op()

    return result_stack[0]

if __name__ == '__main__':
    sample_values = [
        ("True or False", True),
        ("not (True and False)", True),
        ("(True and False) or (False and True)", False),
        ("not not (True or False)", True)
    ]
    
    for expr, expected in sample_values:
        result = evaluate_nested(expr)
        print(f"{expr} -> {result}, Expected: {expected}")