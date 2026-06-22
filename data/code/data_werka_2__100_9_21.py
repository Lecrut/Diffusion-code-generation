import ast
import operator

def is_valid_boolean_expression(expr: str) -> bool:
    try:
        tree = ast.parse(expr, mode='eval')
        return isinstance(tree.body, (ast.BoolOp, ast.Compare, ast.UnaryOp, ast.Constant, ast.Name))
    except SyntaxError:
        return False
    except Exception:
        return False

if __name__ == '__main__':
    samples = [
        "True and False",
        "1 < 2",
        "not True",
        "True",
        "invalid syntax here",
        "1 + 1",
        "True or (False and True)"
    ]
    for sample in samples:
        result = is_valid_boolean_expression(sample)
        print(result)