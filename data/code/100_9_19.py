import ast

def is_valid_boolean_expression(expression):
    try:
        tree = ast.parse(expression, mode='eval')
        if isinstance(tree.body, (ast.NameConstant, ast.UnaryOp)):
            return True
        else:
            return False
    except SyntaxError:
        return False

if __name__ == '__main__':
    print(is_valid_boolean_expression("True"))
    print(is_valid_boolean_expression("False"))
    print(is_valid_boolean_expression("not True"))
    print(is_valid_boolean_expression("and True"))
    print(is_valid_boolean_expression("or False"))
    print(is_valid_boolean_expression("1 + 2"))