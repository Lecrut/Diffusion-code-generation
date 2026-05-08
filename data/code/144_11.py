import re
def evaluate_expression(P, Q, expression):
    variables = {'P': P, 'Q': Q}
    def substitute(match):
        token = match.group(0)
        if token in variables:
            return str(variables[token])
        return token
    expression = expression.replace('AND', '&&').replace('OR', '||').replace('NOT', '!')
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    expression = ' '.join(expression.split())
    tokens = expression.split()
    result_stack = []
    operator_stack = []
    def apply_op():
        op = operator_stack.pop()
        if op == 'NOT':
            operand = result_stack.pop()
            result_stack.append(not operand)
        elif op == '&&':
            op2 = result_stack.pop()
            op1 = result_stack.pop()
            result_stack.append(op1 and op2)
        elif op == '||':
            op2 = result_stack.pop()
            op1 = result_stack.pop()
            result_stack.append(op1 or op2)
    for token in tokens:
        if token in variables:
            result_stack.append(variables[token])
        elif token in ('&&', '||', '!'):
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                apply_op()
            operator_stack.pop()
        else:
            if token == 'NOT':
                operator_stack.append(token)
            else:
                result_stack.append(eval(token))
    while operator_stack:
        apply_op()
    if not result_stack:
        return False
    return result_stack[0]
if __name__ == '__main__':
    P_val = True
    Q_val = False
    test_cases = [
        ('P AND Q', True, False),
        ('(P OR Q)', True, True),
        ('(P OR Q) NOT P', True, False),
        ('NOT P', True, False),
        ('P AND (Q OR NOT P)', True, False),
        ('(P OR Q) AND NOT P', True, False),
        ('P OR Q', True, True),
    ]
    for expr, P_in, Q_in in test_cases:
        result = evaluate_expression(P_in, Q_in, expr)
        print(f"P={P_in}, Q={Q_in}, Expression: '{expr}' -> Result: {result}")