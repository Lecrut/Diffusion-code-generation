import ast
import operator
from typing import Any

def evaluate_boolean_expression(expression: str) -> bool:
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
        ast.List,
        ast.Tuple,
        ast.Dict,
        ast.Set,
        ast.Ellipsis,
        ast.Num,
        ast.Str,
        ast.NameConstant,
    )
    def check_node(n: Any) -> bool:
        if isinstance(n, allowed_types):
            return True
        if isinstance(n, ast.Expr):
            return check_node(n.value)
        if isinstance(n, ast.Expression):
            return check_node(n.body)
        if isinstance(n, ast.BoolOp):
            return all(check_node(v) for v in n.values)
        if isinstance(n, ast.UnaryOp):
            return check_node(n.operand)
        if isinstance(n, ast.Compare):
            return check_node(n.left) and all(check_node(c) for c in n.comparators)
        if isinstance(n, ast.BinOp):
            return check_node(n.left) and check_node(n.right)
        if isinstance(n, ast.Call):
            return check_node(n.func) and all(check_node(a) for a in n.args)
        if isinstance(n, ast.Subscript):
            return check_node(n.value) and check_node(n.slice)
        if isinstance(n, ast.Attribute):
            return check_node(n.value)
        if isinstance(n, ast.List):
            return all(check_node(e) for e in n.elts)
        if isinstance(n, ast.Tuple):
            return all(check_node(e) for e in n.elts)
        if isinstance(n, ast.Dict):
            return all(check_node(k) and check_node(v) for k, v in zip(n.keys, n.values))
        if isinstance(n, ast.Set):
            return all(check_node(e) for e in n.elts)
        if isinstance(n, ast.Name):
            return True
        if isinstance(n, ast.Constant):
            return True
        if isinstance(n, ast.Num):
            return True
        if isinstance(n, ast.Str):
            return True
        if isinstance(n, ast.NameConstant):
            return True
        if isinstance(n, ast.Ellipsis):
            return True
        return False
    return check_node(node)

def main() -> None:
    samples = [
        "True and False",
        "not True",
        "1 == 1",
        "True or (False and True)",
        "invalid expression",
        "1 + 2",
        "True and",
        "",
        "   ",
        "True and False or True",
    ]
    results = [evaluate_boolean_expression(s) for s in samples]
    for s, r in zip(samples, results):
        print(f"{repr(s):30} -> {r}")

if __name__ == '__main__':
    main()