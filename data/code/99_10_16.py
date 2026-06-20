import ast

def print_ast(expression):
    try:
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
    except SyntaxError as e:
        print(f"Syntax error in expression: {e}")

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)