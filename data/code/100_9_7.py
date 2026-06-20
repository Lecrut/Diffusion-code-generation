import ast

def is_valid_boolean_expression(expression):
    try:
        parsed = ast.parse(expression, mode='eval')
        return isinstance(parsed.body, (ast.BoolOp, ast.Compare))
    except SyntaxError:
        return False
if __name__ == '__main__':
    print(is_valid_boolean_expression('True and False'))
    print(is_valid_boolean_expression('x > 5'))
    print(is_valid_boolean_expression('not x'))
    print(is_valid_boolean_expression('x + y'))