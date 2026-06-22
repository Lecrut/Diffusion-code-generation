import ast
import operator

def is_valid_boolean_expression(expression: str) -> bool:
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
    )
    
    def check_node(n):
        if isinstance(n, ast.Constant):
            if isinstance(n.value, bool):
                return True
            return False
        if isinstance(n, ast.Name):
            return n.id in ('True', 'False')
        if isinstance(n, ast.BoolOp):
            return all(check_node(v) for v in n.values)
        if isinstance(n, ast.UnaryOp):
            if isinstance(n.op, (ast.Not,)):
                return check_node(n.operand)
            return False
        if isinstance(n, ast.Compare):
            return all(check_node(c) for c in n.comparators)
        if isinstance(n, ast.BinOp):
            if isinstance(n.op, (ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.Is, ast.IsNot, ast.In, ast.NotIn)):
                return check_node(n.left) and all(check_node(c) for c in n.comparators)
            return False
        if isinstance(n, ast.Call):
            return check_node(n.func) and all(check_node(a) for a in n.args)
        if isinstance(n, ast.List):
            return all(check_node(e) for e in n.elts)
        if isinstance(n, ast.Tuple):
            return all(check_node(e) for e in n.elts)
        if isinstance(n, ast.Dict):
            return all(check_node(k) and check_node(v) for k, v in zip(n.keys, n.values))
        if isinstance(n, ast.Set):
            return all(check_node(e) for e in n.elts)
        if isinstance(n, ast.Subscript):
            return check_node(n.value) and check_node(n.slice)
        if isinstance(n, ast.Attribute):
            return check_node(n.value)
        if isinstance(n, ast.Index):
            return check_node(n.value)
        if isinstance(n, ast.Slice):
            lower = check_node(n.lower) if n.lower else True
            upper = check_node(n.upper) if n.upper else True
            step = check_node(n.step) if n.step else True
            return lower and upper and step
        if isinstance(n, ast.FormattedValue):
            return check_node(n.value)
        if isinstance(n, ast.JoinedStr):
            return all(check_node(v) if isinstance(v, ast.FormattedValue) else True for v in n.values)
        if isinstance(n, ast.Num):
            return False
        if isinstance(n, ast.Str):
            return False
        if isinstance(n, ast.NameConstant):
            return isinstance(n.value, bool)
        return False

    return check_node(node.body)

if __name__ == '__main__':
    samples = [
        "True and False",
        "not True",
        "1 == 1",
        "True or False",
        "invalid syntax here",
        "True and",
        "2 + 2",
        "True if True else False",
    ]
    
    for sample in samples:
        result = is_valid_boolean_expression(sample)
        print(result)