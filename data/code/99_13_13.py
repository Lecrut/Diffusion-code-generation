def validate_flags(flag_a, flag_b):
    if not isinstance(flag_a, bool) or not isinstance(flag_b, bool):
        raise ValueError('Both flags must be boolean')
    return True

def evaluate_conditions(cond1, cond2, operator):
    if operator == 'and':
        return cond1 and cond2
    elif operator == 'or':
        return cond1 or cond2
    else:
        raise ValueError('Invalid operator')

if __name__ == '__main__':
    a = True
    b = False
    validate_flags(a, b)
    result_and = evaluate_conditions(a, b, 'and')
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Result of (a and b): {result_and}")

    c = True
    d = False
    validate_flags(c, d)
    result_or = evaluate_conditions(c, d, 'or')
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"Result of (c or d): {result_or}")