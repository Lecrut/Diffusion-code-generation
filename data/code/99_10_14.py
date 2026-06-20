import ast

def print_ast(expression):
    tree = ast.parse(expression)
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            print(f"{node.left} {type(node.op).__name__} {node.right}")
        elif isinstance(node, ast.UnaryOp):
            print(f"{type(node.op).__name__} {node.operand}")

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)