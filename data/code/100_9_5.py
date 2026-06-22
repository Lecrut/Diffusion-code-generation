import ast
import operator
import re

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
        ast.ExtSlice,
        ast.Yield,
        ast.YieldFrom,
        ast.GeneratorExp,
        ast.ListComp,
        ast.SetComp,
        ast.DictComp,
        ast.comprehension,
        ast.IfExp,
        ast.DictComp,
        ast.SetComp,
        ast.ListComp,
        ast.GeneratorExp,
        ast.arguments,
        ast.arg,
        ast.keyword,
        ast.alias,
        ast.withitem,
        ast.excepthandler,
        ast.match_case,
        ast.match_value,
        ast.match_singleton,
        ast.match_sequence,
        ast.match_mapping,
        ast.match_class,
        ast.match_star,
        ast.match_as,
        ast.match_or,
        ast.match_capture,
        ast.match_wildcard,
        ast.match_or_pattern,
        ast.match_sequence_pattern,
        ast.match_mapping_pattern,
        ast.match_class_pattern,
        ast.match_star_pattern,
        ast.match_as_pattern,
        ast.match_or_pattern,
        ast.match_capture_pattern,
        ast.match_wildcard_pattern,
    )
    for node in ast.walk(node):
        if not isinstance(node, allowed_types):
            return False
    return True

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
    for sample in samples:
        result = is_valid_boolean_expression(sample)
        print(result)