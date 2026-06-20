import ast

def print_ast(expression):
    tree = ast.parse(expression)
    print(ast.dump(tree))

if __name__ == '__main__':
    expression = "not a and b or c"
    print_ast(expression)