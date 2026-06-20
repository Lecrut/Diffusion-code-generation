import ast

def evaluate_boolean_expression(expression):
    try:
        return eval(expression)
    except SyntaxError:
        return "Invalid expression"

if __name__ == '__main__':
    print(evaluate_boolean_expression("True and False"))
    print(evaluate_boolean_expression("10 > 5 or 3 < 2"))
    print(evaluate_boolean_expression("not (1 == 1)"))
    print(evaluate_boolean_expression("(3 + 4) * 2 == 14"))
    print(evaluate_boolean_expression("invalid expression"))