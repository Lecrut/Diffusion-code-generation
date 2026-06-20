def evaluate_flags(flag1, flag2, operator):
    if operator == 'and':
        return flag1 and flag2
    elif operator == 'or':
        return flag1 or flag2
    else:
        raise ValueError('Unsupported operator')

if __name__ == '__main__':
    a = True
    b = False
    result_and = evaluate_flags(a, b, 'and')
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Result of (a and b): {result_and}")

    c = True
    d = False
    result_or = evaluate_flags(c, d, 'or')
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"Result of (c or d): {result_or}")