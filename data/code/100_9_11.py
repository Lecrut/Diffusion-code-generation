import ast

def is_valid_boolean_expression(expression):
    try:
        tree = ast.parse(expression)
        if isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, (ast.NameConstant, ast.UnaryOp)):
            return True
        else:
            return False
    except SyntaxError:
        return False

if __name__ == '__main__':
    test_cases = {
        "True": True,
        "False": True,
        "not True": True,
        "and True": False,
        "or False": False,
        "1 + 2": False,
        "(True and False) or not True": True
    }
    
    for expression, expected in test_cases.items():
        result = is_valid_boolean_expression(expression)
        print(f"Expression: {expression}, Expected: {expected}, Result: {result}")