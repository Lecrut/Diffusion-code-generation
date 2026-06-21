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
        ast.ExtSlice,
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
        ast.keyword,
        ast.arguments,
        ast.arg,
        ast.arguments,
        ast.arguments,
        ast.arguments,
        ast.arguments,
        ast.arguments,
    )
    def check_node(node):
        if isinstance(node, allowed_types):
            return True
        if isinstance(node, ast.Expr):
            return check_node(node.value)
        if isinstance(node, ast.Expression):
            return check_node(node.body)
        if isinstance(node, ast.BoolOp):
            return all(check_node(val) for val in node.values)
        if isinstance(node, ast.UnaryOp):
            return check_node(node.operand)
        if isinstance(node, ast.Compare):
            return check_node(node.left) and all(check_node(comp) for comp in node.comparators)
        if isinstance(node, ast.BinOp):
            return check_node(node.left) and check_node(node.right)
        if isinstance(node, ast.Call):
            return check_node(node.func) and all(check_node(arg) for arg in node.args) and all(check_node(val) for val in node.keywords)
        if isinstance(node, ast.Subscript):
            return check_node(node.value) and check_node(node.slice)
        if isinstance(node, ast.Attribute):
            return check_node(node.value)
        if isinstance(node, ast.Index):
            return check_node(node.value)
        if isinstance(node, ast.Slice):
            return check_node(node.lower) if node.lower else True and check_node(node.upper) if node.upper else True and check_node(node.step) if node.step else True
        if isinstance(node, ast.ExtSlice):
            return all(check_node(dim) for dim in node.dims)
        if isinstance(node, ast.List):
            return all(check_node(el) for el in node.elts)
        if isinstance(node, ast.Tuple):
            return all(check_node(el) for el in node.elts)
        if isinstance(node, ast.Dict):
            return all(check_node(key) if key else True for key in node.keys) and all(check_node(val) for val in node.values)
        if isinstance(node, ast.Set):
            return all(check_node(el) for el in node.elts)
        if isinstance(node, ast.FormattedValue):
            return check_node(node.value)
        if isinstance(node, ast.JoinedStr):
            return all(check_node(val) if isinstance(val, ast.FormattedValue) else True for val in node.values)
        if isinstance(node, ast.Num):
            return True
        if isinstance(node, ast.Str):
            return True
        if isinstance(node, ast.Bytes):
            return True
        if isinstance(node, ast.Ellipsis):
            return True
        if isinstance(node, ast.NameConstant):
            return True
        if isinstance(node, ast.keyword):
            return check_node(node.value) if node.value else True
        if isinstance(node, ast.arguments):
            return all(check_node(arg) for arg in node.args) and all(check_node(arg) for arg in node.kwonlyargs)
        if isinstance(node, ast.arg):
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
        "True if True else False",
    ]
    for sample in samples:
        result = is_valid_boolean_expression(sample)
        print(result)