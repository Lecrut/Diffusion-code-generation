import ast
import operator
from typing import Any

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
        ast.Dict,
        ast.Set,
        ast.FormattedValue,
        ast.JoinedStr,
        ast.Num,
        ast.Str,
        ast.Bytes,
        ast.Ellipsis,
        ast.NameConstant,
        ast.ExtSlice,
        ast.Yield,
        ast.YieldFrom,
        ast.GeneratorExp,
        ast.ListComp,
        ast.SetComp,
        ast.DictComp,
        ast.IfExp,
        ast.DictComp,
        ast.ExceptHandler,
        ast.arguments,
        ast.arg,
        ast.keyword,
        ast.alias,
        ast.withitem,
        ast.comprehension,
        ast.arg,
        ast.arguments,
        ast.keyword,
        ast.alias,
        ast.withitem,
        ast.comprehension,
    )
    def check_node(n: Any) -> bool:
        if isinstance(n, allowed_types):
            return True
        if isinstance(n, ast.AST):
            for child in ast.iter_child_nodes(n):
                if not check_node(child):
                    return False
            return True
        return False
    return check_node(node)

if __name__ == '__main__':
    samples = [
        "True and False",
        "not True",
        "1 == 1",
        "True or (False and True)",
        "invalid syntax here",
        "",
        "1 + 1",
        "True and",
    ]
    for s in samples:
        result = is_valid_boolean_expression(s)
        print(result)