def validate_boolean_expression(expr):
    if not isinstance(expr, bool):
        raise ValueError("Boolean expression must be a boolean value")

def combine_boolean_expressions(expr1, expr2):
    validate_boolean_expression(expr1)
    validate_boolean_expression(expr2)
    
    return (expr1 and not expr2) or (not expr1 and expr2)

if __name__ == '__main__':
    sample_expr1 = True
    sample_expr2 = False
    result = combine_boolean_expressions(sample_expr1, sample_expr2)
    print(result)

    sample_expr1 = False
    sample_expr2 = True
    result = combine_boolean_expressions(sample_expr1, sample_expr2)
    print(result)

    sample_expr1 = True
    sample_expr2 = True
    result = combine_boolean_expressions(sample_expr1, sample_expr2)
    print(result)

    sample_expr1 = False
    sample_expr2 = False
    result = combine_boolean_expressions(sample_expr1, sample_expr2)
    print(result)