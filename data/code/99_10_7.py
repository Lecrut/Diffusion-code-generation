import ast

def print_ast(expression):
    tree = ast.parse(expression)
    def visit(node):
        if isinstance(node, ast.BoolOp):
            operator = type(node.op).__name__
            operands = [visit(operand) for operand in node.values]
            return f"BoolOp: {operator}({', '.join(operands)})"
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            operand = visit(node.operand)
            return f"Not: {operand}"
        elif isinstance(node, ast.BinOp):
            operator = type(node.op).__name__
            left = visit(node.left)
            right = visit(node.right)
            return f"BinOp: {operator}({left}, {right})"
        else:
            return str(node)
    print(visit(tree.body[0]))

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)