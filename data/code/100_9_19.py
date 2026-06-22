import ast

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
        ast.Del,
        ast.Starred,
        ast.keyword,
        ast.expr,
        ast.excepthandler,
        ast.AST,
        ast.arg,
        ast.arguments,
        ast.vararglist,
        ast.slice,
        ast.expr_context,
        ast.operator,
        ast.unaryop,
        ast.cmpop,
        ast.boolop,
        ast.boolop,
        ast.boolop,
        ast.boolop,
    )
    for node_type in ast.walk(node):
        if not isinstance(node_type, allowed_types):
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "True and False",
        "not True",
        "1 == 1",
        "True or False",
        "invalid syntax here",
        "True and",
        "",
        "1 + 1",
    ]
    results = []
    for case in test_cases:
        results.append(is_valid_boolean_expression(case))
    print(results)