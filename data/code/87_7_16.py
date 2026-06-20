def combine_boolean_expressions(expr1, expr2):
    return (expr1 and not expr2) or (not expr1 and expr2)

if __name__ == '__main__':
    sample_exprs = {
        'true_true': (True, True),
        'true_false': (True, False),
        'false_true': (False, True),
        'false_false': (False, False)
    }
    
    for label, (expr1, expr2) in sample_exprs.items():
        result = combine_boolean_expressions(expr1, expr2)
        print(f"{label}: {result}")