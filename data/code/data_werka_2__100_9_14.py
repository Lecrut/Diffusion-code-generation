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
        ast.List,
        ast.Tuple,
        ast.Set,
        ast.Dict,
        ast.Ellipsis,
        ast.Num,
        ast.Str,
        ast.Bytes,
        ast.NameConstant,
    )
    def check_node(n):
        if isinstance(n, ast.AST):
            return any(isinstance(n, t) for t in allowed_types)
        return False
    return check_node(node)

import ast

if __name__ == '__main__':
    print(is_valid_boolean_expression("True and False"))
    print(is_valid_boolean_expression("1 == 1"))
    print(is_valid_boolean_expression("invalid syntax"))
    print(is_valid_boolean_expression(""))