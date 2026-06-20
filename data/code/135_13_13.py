def evaluate_expression(expression, inputs):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            sub_expr = ''
            while stack[-1] != '(':
                sub_expr = stack.pop() + sub_expr
            stack.pop()
            stack.append(evaluate_expression(sub_expr, inputs))
        elif char == '0' or char == '1':
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '&':
                stack.append(a and b)
            elif char == '|':
                stack.append(a or b)
    return stack[0]

def is_equivalent(expr1, expr2):
    inputs = [False, True]
    for a in inputs:
        for b in inputs:
            for c in inputs:
                if evaluate_expression(expr1, {'a': a, 'b': b, 'c': c}) != evaluate_expression(expr2, {'a': a, 'b': b, 'c': c}):
                    return False
    return True

if __name__ == '__main__':
    expr1 = '(a & b) | (c & !a)'
    expr2 = '!a & b | c'
    print(is_equivalent(expr1, expr2))