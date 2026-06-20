import ast

OPERATOR_NAMES = {
    ast.And: 'and',
    ast.Or: 'or',
    ast.Not: 'not'
}

def print_ast(expression):
    tree = ast.parse(expression, mode='eval')
    for node in ast.walk(tree):
        if isinstance(node, (ast.BoolOp, ast.UnaryOp)):
            print(f"{OPERATOR_NAMES[type(node)]}: {ast.dump(node.operand)}")

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)