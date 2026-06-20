import ast

def print_ast(expression):
    try:
        tree = ast.parse(expression)
        def walk(node):
            if isinstance(node, ast.BoolOp):
                operator = type(node.op).__name__
                operands = [walk(operand) for operand in node.values]
                return f"BoolOp: {operator}({', '.join(operands)})"
            elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
                operand = walk(node.operand)
                return f"Not: {operand}"
            elif isinstance(node, ast.BinOp):
                operator = type(node.op).__name__
                left = walk(node.left)
                right = walk(node.right)
                return f"BinOp: {operator}({left}, {right})"
            else:
                return str(node)
        print(walk(tree.body[0].value))
    except SyntaxError as e:
        print(f"Syntax error: {e}")

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)