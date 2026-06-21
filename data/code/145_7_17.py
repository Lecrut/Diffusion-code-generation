def compute_expression(a, b, c, d):
    result = False
    if a:
        result = True
    elif b and not c:
        result = False
    else:
        result = c or d
    return result

if __name__ == '__main__':
    sample_values = {
        'a': True,
        'b': False,
        'c': True,
        'd': False
    }
    print(compute_expression(**sample_values))