def evaluate_expression():
    x = True
    y = False
    z = True
    if not isinstance(x, bool) or not isinstance(y, bool) or (not isinstance(z, bool)):
        raise ValueError('Inputs must be boolean values')
    result = x and y or z
    return result
if __name__ == '__main__':
    print(evaluate_expression())