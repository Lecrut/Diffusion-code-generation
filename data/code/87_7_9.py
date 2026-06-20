def combine_boolean_expressions(expr1, expr2):
    return (expr1 and not expr2) or (not expr1 and expr2)

if __name__ == '__main__':
    sample_exprs = {
        'True-False': (True, False),
        'False-True': (False, True),
        'True-True': (True, True),
        'False-FALSE': (False, False)
    }
    
    for label, (a, b) in sample_exprs.items():
        result = combine_boolean_expressions(a, b)
        print(f'{label}: {result}')