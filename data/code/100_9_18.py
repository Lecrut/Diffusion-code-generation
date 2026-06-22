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
        ast.Set,
        ast.Dict,
        ast.Ellipsis,
        ast.Num,
        ast.Str,
        ast.Bytes,
    )
    def check_node(node):
        if isinstance(node, allowed_types):
            if isinstance(node, ast.BoolOp):
                return all(check_node(val) for val in node.values)
            if isinstance(node, ast.UnaryOp):
                return check_node(node.operand)
            if isinstance(node, ast.Compare):
                return all(check_node(val) for val in node.comparators) and check_node(node.left)
            if isinstance(node, ast.BinOp):
                return check_node(node.left) and check_node(node.right)
            if isinstance(node, ast.Call):
                return check_node(node.func) and all(check_node(arg) for arg in node.args) and all(check_node(arg) for arg in node.keywords)
            if isinstance(node, ast.Subscript):
                return check_node(node.value) and check_node(node.slice)
            if isinstance(node, ast.Attribute):
                return check_node(node.value)
            if isinstance(node, ast.Index):
                return check_node(node.value)
            if isinstance(node, ast.Slice):
                return check_node(node.lower) if node.lower else True
            if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
                return all(check_node(el) for el in node.elts)
            if isinstance(node, ast.Dict):
                return all(check_node(k) for k in node.keys) and all(check_node(v) for v in node.values)
            return True
        return False
    return check_node(node)

if __name__ == '__main__':
    test_cases = [
        "True and False",
        "not True",
        "1 < 2 and 3 > 4",
        "True or (False and True)",
        "invalid syntax",
        "",
        "None",
        "True if True else False",
    ]
    for case in test_cases:
        result = is_valid_boolean_expression(case)
        print(result)