def evaluate_boolean_expression(expression, variables):
    def parse_and_evaluate(expr):
        if expr.isalpha():
            return variables[expr]
        elif expr.startswith('(') and expr.endswith(')'):
            return eval(expr, {'__builtins__': None}, variables)
        else:
            op = expr.split()[1]
            left = parse_and_evaluate(expr.split()[0])
            right = parse_and_evaluate(expr.split()[2])
            if op == 'and':
                return left and right
            elif op == 'or':
                return left or right

    return parse_and_evaluate(expression)

if __name__ == '__main__':
    expression = '((A and B) or C)'
    variables = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(expression, variables))