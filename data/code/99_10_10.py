import ast

def print_ast(expression):
    tree = ast.parse(expression)
    for node in ast.walk(tree):
        if isinstance(node, ast.BoolOp):
            print(f"BoolOp: {type(node.op).__name__}")
        elif isinstance(node, ast.UnaryOp):
            print(f"UnaryOp: {type(node.op).__name__}")
        elif isinstance(node, ast.NameConstant):
            print(f"NameConstant: {node.value}")

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)