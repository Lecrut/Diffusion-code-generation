def evaluate_boolean_expression(expression):
    return eval(expression)

if __name__ == '__main__':
    print(evaluate_boolean_expression("True and False or not True"))
    print(evaluate_boolean_expression(not (False or True) and True))
    print(evaluate_boolean_expression(True and not (False and True)))
    print(evaluate_boolean_expression((True or False) and (not False)))