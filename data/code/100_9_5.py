import ast

def is_valid_boolean_expression(expression):
    try:
        parsed = ast.parse(expression, mode='eval')
        if isinstance(parsed.body, (ast.BoolOp, ast.Compare)):
            return True
        return False
    except SyntaxError:
        return False
if __name__ == '__main__':
    sample_values = ['True', 'False', '1 > 2', 'a and b', 'not c', 'x or y', '3 + 4', 'hello']
    for value in sample_values:
        print(f"'{value}': {is_valid_boolean_expression(value)}")