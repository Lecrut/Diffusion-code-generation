import ast

def evaluate_boolean_expression(expression):
    try:
        parsed_expr = ast.parse(expression, mode='eval').body
        result = eval(compile(parsed_expr, filename='<ast>', mode='eval'))
        return result
    except (SyntaxError, NameError, TypeError) as e:
        print(f'Error evaluating expression: {e}')
        return None
if __name__ == '__main__':
    sample_expression = '3 > 2 and not False'
    print(evaluate_boolean_expression(sample_expression))