def evaluate_boolean_expression(expression):
    try:
        return eval(expression)
    except SyntaxError:
        return 'Syntax error in expression'

if __name__ == '__main__':
    print(evaluate_boolean_expression('3 > 2 and 5 < 10'))
    print(evaluate_boolean_expression('not (3 == 4)'))
    print(evaluate_boolean_expression('(3 + 5) * 2'))
    try:
        print(evaluate_boolean_expression('10 / 0'))
    except ZeroDivisionError as e:
        print(f'Caught exception: {e}')