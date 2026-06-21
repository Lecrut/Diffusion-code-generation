import ast
import operator

def is_valid_boolean_expression(expr: str) -> bool:
    try:
        node = ast.parse(expr, mode='eval')
        if not isinstance(node.body, (ast.Compare, ast.BoolOp, ast.UnaryOp, ast.Constant)):
            return False
        if isinstance(node.body, ast.Constant):
            if not isinstance(node.body.value, bool):
                return False
        if isinstance(node.body, ast.Compare):
            for op in node.body.ops:
                if not isinstance(op, (ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.In, ast.NotIn, ast.Is, ast.IsNot)):
                    return False
        if isinstance(node.body, ast.BoolOp):
            if not isinstance(node.body.op, (ast.And, ast.Or)):
                return False
        if isinstance(node.body, ast.UnaryOp):
            if not isinstance(node.body.op, (ast.Not, ast.Invert, ast.UAdd, ast.USub)):
                return False
        return True
    except SyntaxError:
        return False
    except Exception:
        return False

if __name__ == '__main__':
    samples = [
        "True and False",
        "1 == 1",
        "not True",
        "True or False",
        "invalid syntax here",
        "42",
        "True",
        "False",
        "1 < 2 and 3 > 4",
        "x == y"
    ]
    for sample in samples:
        result = is_valid_boolean_expression(sample)
        print(result)