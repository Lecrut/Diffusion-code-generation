def evaluate_expression(expression, variables):
    def parse_and_evaluate(expr):
        if expr.isdigit():
            return bool(int(expr))
        elif expr.isalpha():
            return variables[expr]
        else:
            op = expr[1:-1].split()
            left = parse_and_evaluate(op[0])
            right = parse_and_evaluate(op[2])
            if op[1] == 'and':
                return left and right
            elif op[1] == 'or':
                return left or right

    return parse_and_evaluate(expression)

if __name__ == '__main__':
    expression = '((A and B) or C)'
    variables = {'A': True, 'B': False, 'C': True}
    print(evaluate_expression(expression, variables))