def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    def parse_and_eval(expr):
        if expr.islower():
            return variables[expr]
        elif expr.startswith('(') and expr.endswith(')'):
            return eval(expr[1:-1], None, {'and': lambda a, b: a and b, 'or': lambda a, b: a or b})
        else:
            raise ValueError("Invalid expression")

    return parse_and_eval(expression)

if __name__ == '__main__':
    sample_expression = '((A and B) or C)'
    sample_variables = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(sample_expression, sample_variables))