def check_boolean_expression(expression):
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
    )
    def validate_node(n):
        if isinstance(n, allowed_types):
            if isinstance(n, ast.BoolOp):
                for val in n.values:
                    if not validate_node(val):
                        return False
                return True
            if isinstance(n, ast.UnaryOp):
                return validate_node(n.operand)
            if isinstance(n, ast.BinOp):
                return validate_node(n.left) and validate_node(n.right)
            if isinstance(n, ast.Compare):
                for comp in n.comparators:
                    if not validate_node(comp):
                        return False
                return True
            if isinstance(n, ast.Call):
                for arg in n.args:
                    if not validate_node(arg):
                        return False
                return True
            if isinstance(n, ast.Subscript):
                return validate_node(n.value) and validate_node(n.slice)
            if isinstance(n, ast.Attribute):
                return validate_node(n.value)
            return True
        return False
    return validate_node(node)

import ast

if __name__ == '__main__':
    print(check_boolean_expression("True and False"))
    print(check_boolean_expression("not True"))
    print(check_boolean_expression("1 == 1"))
    print(check_boolean_expression("invalid expression"))
    print(check_boolean_expression(""))
    print(check_boolean_expression("True or (False and True)"))
    print(check_boolean_expression("5 > 3 and 2 < 4"))
    print(check_boolean_expression("True if True else False"))
    print(check_boolean_expression("len([1, 2]) > 0"))
    print(check_boolean_expression("None"))
    print(check_boolean_expression("True"))
    print(check_boolean_expression("False"))
    print(check_boolean_expression("not not True"))
    print(check_boolean_expression("True and not False"))
    print(check_boolean_expression("not (True and False)"))
    print(check_boolean_expression("True or False or True"))
    print(check_boolean_expression("False and False and False"))
    print(check_boolean_expression("not (not not not True)"))
    print(check_boolean_expression("1 == 1 and 2 == 2 or 3 == 3"))
    print(check_boolean_expression("True and (False or True)"))
    print(check_boolean_expression("not True and False"))
    print(check_boolean_expression("True or not False"))
    print(check_boolean_expression("not (True or False)"))
    print(check_boolean_expression("not (False and True)"))
    print(check_boolean_expression("True and False or True"))
    print(check_boolean_expression("True or False and True"))
    print(check_boolean_expression("not True or False"))
    print(check_boolean_expression("True and not False or True"))
    print(check_boolean_expression("not (True and False) or True"))
    print(check_boolean_expression("True and (not False or True)"))
    print(check_boolean_expression("not (True and (False or True))"))
    print(check_boolean_expression("True or (False and (not True))"))
    print(check_boolean_expression("not (True or (False and True))"))
    print(check_boolean_expression("True and not (False or True)"))
    print(check_boolean_expression("not (True and not (False or True))"))
    print(check_boolean_expression("True or not (False and not True)"))
    print(check_boolean_expression("not (True or not (False and True))"))
    print(check_boolean_expression("True and not (False or not True)"))
    print(check_boolean_expression("not (True and not (False or True))"))
    print(check_boolean_expression("True or not (False and not (True or False))"))
    print(check_boolean_expression("not (True or not (False and (True or False)))"))
    print(check_boolean_expression("True and not (False or not (True and False))"))
    print(check_boolean_expression("not (True and not (False or (True and False)))"))
    print(check_boolean_expression("True or not (False and not (True or False))"))