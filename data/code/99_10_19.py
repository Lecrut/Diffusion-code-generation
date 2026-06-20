import ast

def print_ast(expression):
    tree = ast.parse(expression)
    def _print_node(node, depth=0):
        if isinstance(node, ast.BoolOp):
            operator = type(node.op).__name__
            operands = [_print_node(operand, depth + 1) for operand in node.values]
            return f"{' ' * depth}BoolOp: {operator}({', '.join(operands)})"
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            operand = _print_node(node.operand, depth + 1)
            return f"{' ' * depth}Not: {operand}"
        elif isinstance(node, ast.BinOp):
            operator = type(node.op).__name__
            left = _print_node(node.left, depth + 1)
            right = _print_node(node.right, depth + 1)
            return f"{' ' * depth}BinOp: {operator}({left}, {right})"
        elif isinstance(node, ast.Name):
            return f"{' ' * depth}{node.id}"
        else:
            return str(node)

    print(_print_node(tree.body[0]))

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)