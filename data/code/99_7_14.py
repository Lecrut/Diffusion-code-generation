import ast

def evaluate_boolean_expression(expression):
    try:
        return eval(expression)
    except SyntaxError:
        return "Invalid expression"

if __name__ == '__main__':
    print(evaluate_boolean_expression("2 > 1 and 3 < 4"))
    print(evaluate_boolean_expression("not (True or False)"))
    print(evaluate_boolean_expression("5 == 5 and 6 != 7"))
    print(evaluate_boolean_expression("False or True and False"))
    print(evaluate_boolean_expression("invalid syntax"))