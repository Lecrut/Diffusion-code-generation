import ast

def is_valid_boolean_expression(expression):
    try:
        parsed = ast.parse(expression, mode='eval')
        if isinstance(parsed.body, (ast.And, ast.Or, ast.Not, ast.Compare)):
            return True
        if isinstance(parsed.body, ast.NameConstant):
            return True
        return False
    except SyntaxError:
        return False
if __name__ == '__main__':
    sample_values = ['True', 'False', 'a and b', 'a or b', 'not a', 'a > 5', '1 + 2', 'x = True']
    for value in sample_values:
        print(f'Expression: {value}, Valid: {is_valid_boolean_expression(value)}')