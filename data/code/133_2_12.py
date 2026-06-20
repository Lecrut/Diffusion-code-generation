import ast

def evaluate_boolean_expression(expression):
    return eval(compile(ast.parse(expression).body[0], filename="<ast>", mode="eval"))

if __name__ == '__main__':
    print(evaluate_boolean_expression("True"))
    print(evaluate_boolean_expression("False"))
    print(evaluate_boolean_expression("not True"))
    print(evaluate_boolean_expression("1 == 1"))
    print(evaluate_boolean_expression("2 > 3"))