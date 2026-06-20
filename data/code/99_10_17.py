import ast

class ASTPrinter:
    def __init__(self, expression):
        self.expression = expression
        self.tree = ast.parse(expression)

    def print_ast(self):
        for node in ast.walk(self.tree):
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

if __name__ == '__main__':
    printer = ASTPrinter("not (a and b) or c")
    printer.print_ast()