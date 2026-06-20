import ast

def is_valid_boolean_expression(expression):
    boolean_operators = {'and', 'or', 'not'}
    try:
        tree = ast.parse(expression, mode='eval')
        if isinstance(tree.body, (ast.NameConstant, ast.UnaryOp)):
            return True
        elif isinstance(tree.body, ast.BinOp) and isinstance(tree.body.op, (ast.And, ast.Or)):
            left = is_valid_boolean_expression(ast.unparse(tree.body.left))
            right = is_valid_boolean_expression(ast.unparse(tree.body.right))
            return left and right
        elif isinstance(tree.body, ast.UnaryOp) and isinstance(tree.body.op, ast.Not):
            operand = is_valid_boolean_expression(ast.unparse(tree.body.operand))
            return operand
        else:
            return False
    except SyntaxError:
        return False

if __name__ == '__main__':
    print(is_valid_boolean_expression("True"))
    print(is_valid_boolean_expression("False"))
    print(is_valid_boolean_expression("not True"))
    print(is_valid_boolean_expression("True and False"))
    print(is_valid_boolean_expression("not (True or False)"))