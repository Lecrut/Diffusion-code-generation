def combine_booleans(expr1, expr2):
    if not isinstance(expr1, bool) or not isinstance(expr2, bool):
        raise ValueError("Both expressions must be boolean values")
    return (expr1 and expr2) or (not expr1 and not expr2)

if __name__ == '__main__':
    sample_expr1 = True
    sample_expr2 = False
    result = combine_booleans(sample_expr1, sample_expr2)
    print(result)

    sample_expr1 = False
    sample_expr2 = True
    result = combine_booleans(sample_expr1, sample_expr2)
    print(result)

    sample_expr1 = True
    sample_expr2 = True
    result = combine_booleans(sample_expr1, sample_expr2)
    print(result)

    sample_expr1 = False
    sample_expr2 = False
    result = combine_booleans(sample_expr1, sample_expr2)
    print(result)