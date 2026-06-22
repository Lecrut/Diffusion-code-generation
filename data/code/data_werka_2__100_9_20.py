def is_valid_boolean_expression(expression: str) -> bool:
    if not isinstance(expression, str):
        raise ValueError("Input must be a string")
    if not expression.strip():
        return False
    try:
        node = ast.parse(expression, mode='eval')
    except SyntaxError:
        return False
    allowed_types = (
        ast.Constant,
        ast.Name,
        ast.BoolOp,
        ast.UnaryOp,
        ast.Compare,
        ast.BinOp,
        ast.Call,
        ast.Subscript,
        ast.Attribute,
        ast.Index,
        ast.Slice,
        ast.ExtSlice,
        ast.List,
        ast.Tuple,
        ast.Set,
        ast.Dict,
        ast.Ellipsis,
        ast.GeneratorExp,
        ast.ListComp,
        ast.SetComp,
        ast.DictComp,
        ast.Yield,
        ast.YieldFrom,
        ast.IfExp,
        ast.Lambda,
        ast.Assert,
    )
    def check_node(node):
        if isinstance(node, allowed_types):
            if isinstance(node, ast.Constant):
                if isinstance(node.value, bool):
                    return True
                return False
            if isinstance(node, ast.Name):
                return True
            if isinstance(node, ast.BoolOp):
                return all(check_node(v) for v in node.values)
            if isinstance(node, ast.UnaryOp):
                if isinstance(node.op, (ast.Not,)):
                    return check_node(node.operand)
                return False
            if isinstance(node, ast.Compare):
                return True
            if isinstance(node, ast.BinOp):
                if isinstance(node.op, (ast.And, ast.Or)):
                    return check_node(node.left) and check_node(node.right)
                return False
            if isinstance(node, ast.Call):
                return True
            if isinstance(node, ast.Subscript):
                return check_node(node.value)
            if isinstance(node, ast.Attribute):
                return check_node(node.value)
            if isinstance(node, ast.Index):
                return check_node(node.value)
            if isinstance(node, ast.Slice):
                return True
            if isinstance(node, ast.ExtSlice):
                return True
            if isinstance(node, ast.List):
                return True
            if isinstance(node, ast.Tuple):
                return True
            if isinstance(node, ast.Set):
                return True
            if isinstance(node, ast.Dict):
                return True
            if isinstance(node, ast.Ellipsis):
                return True
            if isinstance(node, ast.GeneratorExp):
                return True
            if isinstance(node, ast.ListComp):
                return True
            if isinstance(node, ast.SetComp):
                return True
            if isinstance(node, ast.DictComp):
                return True
            if isinstance(node, ast.Yield):
                return True
            if isinstance(node, ast.YieldFrom):
                return True
            if isinstance(node, ast.IfExp):
                return check_node(node.test) and check_node(node.body) and check_node(node.orelse)
            if isinstance(node, ast.Lambda):
                return True
            if isinstance(node, ast.Assert):
                return True
            return False
        return False
    return check_node(node)

if __name__ == '__main__':
    import ast
    print(is_valid_boolean_expression("True and False"))
    print(is_valid_boolean_expression("True or not False"))
    print(is_valid_boolean_expression("not (True and False)"))
    print(is_valid_boolean_expression("1 == 1"))
    print(is_valid_boolean_expression("True"))
    print(is_valid_boolean_expression("False"))
    print(is_valid_boolean_expression("True and"))
    print(is_valid_boolean_expression("123"))
    print(is_valid_boolean_expression(""))
    print(is_valid_boolean_expression("   "))
    print(is_valid_boolean_expression(None))