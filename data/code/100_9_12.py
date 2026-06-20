import ast

def is_valid_boolean_expression(expression):
    try:
        tree = ast.parse(expression)
        if len(tree.body) != 1 or not isinstance(tree.body[0], ast.Expr):
            return False
        value = tree.body[0].value
        return isinstance(value, (ast.NameConstant, ast.Compare))
    except SyntaxError:
        return False
if __name__ == '__main__':
    print(is_valid_boolean_expression('True'))
    print(is_valid_boolean_expression('False'))
    print(is_valid_boolean_expression('x > 5'))
    print(is_valid_boolean_expression('x < y'))
    print(is_valid_boolean_expression('x == y'))
    print(is_valid_boolean_expression('x != y'))
    print(is_valid_boolean_expression('x and y'))
    print(is_valid_boolean_expression('x or y'))
    print(is_valid_boolean_expression('not x'))
    print(is_valid_boolean_expression('x + y'))