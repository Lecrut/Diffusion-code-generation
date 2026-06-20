def combine_boolean_expressions(expr1, expr2):
    return (expr1 and not expr2) or (not expr1 and expr2)

if __name__ == '__main__':
    sample_exprs = {
        (True, False): True,
        (False, True): True,
        (True, True): False,
        (False, False): False
    }

    for key, value in sample_exprs.items():
        result = combine_boolean_expressions(*key)
        print(f"combine_boolean_expressions({key[0]}, {key[1]}) = {result}, expected: {value}")