TRUE = True
FALSE = False

def evaluate_nested(expression):
    tokens = expression.split()
    if not tokens:
        return FALSE
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
    for token in tokens:
        if token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                apply_op()
            operator_stack.pop()
        elif token == 'NOT':
            operator_stack.append(token)
        elif token == 'AND':
            operator_stack.append(token)
        else:
            result_stack.append(token == 'True')
    while operator_stack:
        apply_op()
    return result_stack[0]
if __name__ == '__main__':
    test_cases = [('True', TRUE), ('False', FALSE), ('not True', FALSE), ('not False', TRUE), ('True and False', FALSE), ('True and True', TRUE), ('False or True', TRUE), ('False or False', FALSE), ('(True and False) or (True and True)', TRUE)]
    for expression, expected in test_cases:
        result = evaluate_nested(expression)
        print(f'Expression: {expression}, Expected: {expected}, Result: {result}')