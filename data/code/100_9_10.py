import ast

def is_valid_boolean_expression(expression):
    try:
        tree = ast.parse(expression)
        if len(tree.body) != 1:
            return False
        node = tree.body[0]
        if isinstance(node, ast.Expr) and isinstance(node.value, (ast.NameConstant, ast.UnaryOp)):
            return True
        elif isinstance(node, ast.BoolOp):
            for value in node.values:
                if not isinstance(value, (ast.NameConstant, ast.UnaryOp)):
                    return False
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