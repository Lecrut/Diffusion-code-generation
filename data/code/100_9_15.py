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

    boolean_operators = {
        ast.And: 'and',
        ast.Or: 'or'
    }
    comparison_operators = {
        ast.Eq: '==',
        ast.NotEq: '!=',
        ast.Lt: '<',
        ast.LtE: '<=',
        ast.Gt: '>',
        ast.GtE: '>=',
        ast.Is: 'is',
        ast.IsNot: 'is not',
        ast.In: 'in',
        ast.NotIn: 'not in'
    }
    unary_operators = {
        ast.Not: 'not'
    }

    def validate_node(node):
        if isinstance(node, ast.BoolOp):
            if type(node.op) not in boolean_operators:
                return False
            for value in node.values:
                if not validate_node(value):
                    return False
            return True
        elif isinstance(node, ast.Compare):
            if type(node.ops[0]) not in comparison_operators:
                return False
            if not validate_node(node.left):
                return False
            for comparator in node.comparators:
                if not validate_node(comparator):
                    return False
            return True
        elif isinstance(node, ast.UnaryOp):
            if type(node.op) not in unary_operators:
                return False
            if not validate_node(node.operand):
                return False
            return True
        elif isinstance(node, ast.BinOp):
            if not validate_node(node.left):
                return False
            if not validate_node(node.right):
                return False
            return True
        elif isinstance(node, ast.Name):
            return True
        elif isinstance(node, ast.Constant):
            return True
        elif isinstance(node, ast.Attribute):
            if not validate_node(node.value):
                return False
            return True
        elif isinstance(node, ast.Subscript):
            if not validate_node(node.value):
                return False
            if not validate_node(node.slice):
                return False
            return True
        elif isinstance(node, ast.Call):
            if not validate_node(node.func):
                return False
            for arg in node.args:
                if not validate_node(arg):
                    return False
            for kw in node.keywords:
                if not validate_node(kw.value):
                    return False
            return True
        elif isinstance(node, ast.Index):
            return validate_node(node.value)
        else:
            return False

    return validate_node(node)

if __name__ == '__main__':
    test_cases = [
        "True and False",
        "1 > 2",
        "not True",
        "x == 5",
        "True or False",
        "invalid syntax here",
        "1 + 2",
        "5",
        "",
        "True and",
    ]

    for case in test_cases:
        result = is_valid_boolean_expression(case)
        print(result)