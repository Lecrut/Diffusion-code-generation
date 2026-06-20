import ast

def print_ast(expression):
    tree = ast.parse(expression)
    for node in ast.walk(tree):
        if isinstance(node, ast.BoolOp):
            operator = type(node.op).__name__
            operands = [ast.dump(operand) for operand in node.values]
            print(f"BoolOp: {operator}({', '.join(operands)})")
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            operand = ast.dump(node.operand)
            print(f"Not: {operand}")
        elif isinstance(node, ast.BinOp):
            operator = type(node.op).__name__
            left = ast.dump(node.left)
            right = ast.dump(node.right)
            print(f"BinOp: {operator}({left}, {right})")

def validate_expression(expression):
    try:
        ast.parse(expression)
        return True
    except SyntaxError:
        return False

if __name__ == '__main__':
    expression = "not (a and b) or c"
    if validate_expression(expression):
        print_ast(expression)