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
        ast.List,
        ast.Tuple,
        ast.Dict,
        ast.Set,
        ast.Ellipsis,
        ast.Num,
        ast.Str,
        ast.Bytes,
        ast.NameConstant,
    )
    
    def check_node(node_obj):
        if isinstance(node_obj, ast.AST):
            if type(node_obj) not in allowed_types:
                return False
            for child in ast.walk(node_obj):
                if type(child) not in allowed_types:
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
        "invalid expression",
        "True and",
        "",
        "1 + 1",
        "True if True else False",
        "x > 5 and y < 10",
    ]
    
    for sample in samples:
        result = is_valid_boolean_expression(sample)
        print(result)