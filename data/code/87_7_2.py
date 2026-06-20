def combine_boolean_expressions(expr1, expr2):
    return (expr1 and not expr2) or (not expr1 and expr2)

if __name__ == '__main__':
    sample_expr1 = True
    sample_expr2 = False
    result = combine_boolean_expressions(sample_expr1, sample_expr2)
    print(result)