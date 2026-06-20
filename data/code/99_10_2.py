import ast

def print_ast(expression):
    tree = ast.parse(expression)
    for node in ast.walk(tree):
        if isinstance(node, ast.BoolOp):
            print(f"BoolOp: {type(node.op).__name__}")
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            print("UnaryOp: Not")
        elif isinstance(node, ast.BinOp):
            print(f"BinOp: {type(node.op).__name__}")

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)