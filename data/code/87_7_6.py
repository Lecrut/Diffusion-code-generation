def combine_boolean_expressions(expr1, expr2):
    return (expr1 and not expr2) or (not expr1 and expr2)

if __name__ == '__main__':
    boolean_map = {
        'A': True,
        'B': False,
        'C': True,
        'D': True
    }

    result1 = combine_boolean_expressions(boolean_map['A'], boolean_map['B'])
    print(result1)

    result2 = combine_boolean_expressions(boolean_map['C'], boolean_map['D'])
    print(result2)