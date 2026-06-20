def evaluate_boolean_expression(expression):
    a = True
    b = False
    c = True
    result = (a or b) and (not (c and (not a)))
    return result
if __name__ == '__main__':
    print(evaluate_boolean_expression())