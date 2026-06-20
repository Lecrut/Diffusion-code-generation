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
    test_cases = [
        "True",
        "False",
        "not True",
        "and",
        "1 == 1",
        "x and y or z"
    ]
    
    for case in test_cases:
        print(f"Expression: {case}, Valid: {is_valid_boolean_expression(case)}")