def evaluate_boolean_expression():
    a = True
    b = False
    c = True
    result = (a or b) and (not c)
    return result
if __name__ == '__main__':
    print(evaluate_boolean_expression())