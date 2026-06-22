import ast
import operator

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
        ast.Ellipsis,
        ast.NameConstant,
        ast.keyword,
        ast.arguments,
        ast.arg,
        ast.excepthandler,
        ast.alias,
        ast.withitem,
        ast.expr_context,
        ast.cmpop,
        ast.boolop,
        ast.unaryop,
        ast.operator,
        ast.AugStore,
        ast.AugLoad,
        ast.Store,
        ast.Load,
        ast.Param,
    )
    for node in ast.walk(node):
        if not isinstance(node, allowed_types):
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "True and False",
        "not True",
        "1 == 1",
        "True or False",
        "invalid syntax",
        "1 + 2",
        "True and",
        "True and True",
        "False or True",
        "not not True",
        "True == True",
        "False != True",
        "True and False or True",
        "True and (False or True)",
        "True and [1, 2, 3]",
        "True and {1: 2}",
        "True and (1, 2)",
        "True and {1, 2}",
        "True and {1}",
        "True and set()",
        "True and dict()",
        "True and list()",
        "True and tuple()",
        "True and frozenset()",
        "True and range(10)",
        "True and len([1, 2, 3])",
        "True and len({1: 2})",
        "True and len((1, 2))",
        "True and len({1, 2})",
        "True and len({1})",
        "True and len(set())",
        "True and len(dict())",
        "True and len(list())",
        "True and len(tuple())",
        "True and len(frozenset())",
        "True and len(range(10))",
        "True and len(range(0))",
        "True and len(range(1))",
        "True and len(range(2))",
        "True and len(range(3))",
        "True and len(range(4))",
        "True and len(range(5))",
        "True and len(range(6))",
        "True and len(range(7))",
        "True and len(range(8))",
        "True and len(range(9))",
        "True and len(range(10))",
        "True and len(range(11))",
        "True and len(range(12))",
        "True and len(range(13))",
        "True and len(range(14))",
        "True and len(range(15))",
        "True and len(range(16))",
        "True and len(range(17))",
        "True and len(range(18))",
        "True and len(range(19))",
        "True and len(range(20))",
    ]
    for test in test_cases:
        print(f"{test!r:30} -> {is_valid_boolean_expression(test)}")