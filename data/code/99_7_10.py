import ast

def evaluate_boolean_expression(expression):
    try:
        return eval(expression)
    except SyntaxError:
        return "Invalid expression"

if __name__ == '__main__':
    print(evaluate_boolean_expression("2 > 1"))
    print(evaluate_boolean_expression("not True and False"))
    print(evaluate_boolean_expression("(3 + 5) * 2 == 16"))
    print(evaluate_boolean_expression("invalid syntax"))