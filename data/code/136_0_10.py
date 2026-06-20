def validate_boolean_inputs(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Both inputs must be boolean values.')

def logical_and(a, b):
    validate_boolean_inputs(a, b)
    return a and b

def logical_or(a, b):
    validate_boolean_inputs(a, b)
    return a or b

def logical_not(a):
    validate_boolean_inputs(a, a)
    return not a
if __name__ == '__main__':
    a = True
    b = False
    result_and = logical_and(a, b)
    result_or = logical_or(a, b)
    result_not_a = logical_not(a)
    result_not_b = logical_not(b)
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'Logical AND ({a} and {b}): {result_and}')
    print(f'Logical OR ({a} or {b}): {result_or}')
    print(f'Logical NOT of {a}: {result_not_a}')
    print(f'Logical NOT of {b}: {result_not_b}')