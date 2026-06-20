def evaluate_boolean_expression(expression, variables):
    def parse_and_evaluate(expr):
        if expr in variables:
            return variables[expr]
        elif 'and' in expr:
            left, right = expr.split(' and ')
            return parse_and_evaluate(left) and parse_and_evaluate(right)
        elif 'or' in expr:
            left, right = expr.split(' or ')
            return parse_and_evaluate(left) or parse_and_evaluate(right)
        else:
            raise ValueError("Invalid expression")

    return parse_and_evaluate(expression)

if __name__ == '__main__':
    variables = {'A': True, 'B': False, 'C': True}
    expression = '((A and B) or C)'
    result = evaluate_boolean_expression(expression, variables)
    print(result)