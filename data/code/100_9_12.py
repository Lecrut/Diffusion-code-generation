import ast
import operator

def is_valid_boolean_expression(expression: str) -> bool:
    try:
        tree = ast.parse(expression, mode='eval')
        allowed_nodes = {
            ast.Expression,
            ast.BoolOp,
            ast.UnaryOp,
            ast.Compare,
            ast.Constant,
            ast.Name,
            ast.BinOp,
            ast.Add,
            ast.Sub,
            ast.Mult,
            ast.Div,
            ast.FloorDiv,
            ast.Mod,
            ast.Pow,
            ast.LShift,
            ast.RShift,
            ast.BitOr,
            ast.BitXor,
            ast.BitAnd,
            ast.Invert,
            ast.Not,
            ast.UAdd,
            ast.USub,
            ast.Eq,
            ast.NotEq,
            ast.Lt,
            ast.LtE,
            ast.Gt,
            ast.GtE,
            ast.Is,
            ast.IsNot,
            ast.In,
            ast.NotIn,
            ast.And,
            ast.Or,
        }
        
        for node in ast.walk(tree):
            if not isinstance(node, allowed_nodes):
                return False
        return True
    except SyntaxError:
        return False
    except Exception:
        return False

if __name__ == '__main__':
    samples = [
        "True and False",
        "not (1 == 1)",
        "5 > 3 and 2 < 4",
        "True or False",
        "invalid syntax here",
        "1 + 1",
        "True and",
        "not True",
        "False or True",
        "3 == 3",
    ]
    
    results = [is_valid_boolean_expression(s) for s in samples]
    print(results)