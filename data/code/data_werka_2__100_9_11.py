import ast

def is_valid_boolean_expression(expression: str) -> bool:
    if not isinstance(expression, str):
        raise ValueError("Input must be a string")
    if not expression.strip():
        return False
    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError:
        return False
    
    allowed_ops = (
        ast.And,
        ast.Or,
        ast.Not,
        ast.Invert,
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
    )
    
    allowed_nodes = (
        ast.Expression,
        ast.BoolOp,
        ast.Compare,
        ast.UnaryOp,
        ast.Constant,
        ast.Name,
    )
    
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            return False
        if isinstance(node, ast.UnaryOp):
            if not isinstance(node.op, allowed_ops):
                return False
        if isinstance(node, ast.Compare):
            for op in node.ops:
                if not isinstance(op, allowed_ops):
                    return False
            for comp in node.comparators:
                if not isinstance(comp, (ast.Constant, ast.Name)):
                    return False
        if isinstance(node, ast.BoolOp):
            if not isinstance(node.op, (ast.And, ast.Or)):
                return False
            for val in node.values:
                if not isinstance(val, (ast.Constant, ast.Name, ast.Compare, ast.UnaryOp)):
                    return False
        if isinstance(node, ast.Constant):
            if not isinstance(node.value, (bool, int, float, str)):
                return False
        if isinstance(node, ast.Name):
            continue
            
    return True

if __name__ == '__main__':
    samples = [
        "True and False",
        "not True",
        "1 == 1",
        "True or False",
        "invalid syntax here",
        "1 + 2",
        "True and",
        "",
        "x > 5 and y < 10",
    ]
    
    for sample in samples:
        result = is_valid_boolean_expression(sample)
        print(result)