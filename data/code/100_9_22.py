import ast
import operator

def is_valid_boolean_expression(expr: str) -> bool:
    try:
        tree = ast.parse(expr, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, ast.Expression):
                continue
            if isinstance(node, ast.BoolOp):
                continue
            if isinstance(node, ast.Compare):
                continue
            if isinstance(node, ast.UnaryOp):
                if isinstance(node.op, (ast.Invert, ast.Not)):
                    continue
                continue
            if isinstance(node, ast.Constant):
                if isinstance(node.value, bool):
                    continue
                continue
            if isinstance(node, ast.Name):
                continue
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'bool':
                    continue
                continue
            if isinstance(node, ast.BinOp):
                if isinstance(node.op, (ast.BitAnd, ast.BitOr, ast.BitXor)):
                    continue
                continue
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
        "True and",
        "if True",
        "True + False",
        "True and True",
        "5 > 3",
        "x and y"
    ]
    for sample in samples:
        result = is_valid_boolean_expression(sample)
        print(result)