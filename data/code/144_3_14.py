def truth_table(booleans):
    from itertools import product
    return [[bool_val for bool_val in row] for row in product(*booleans)]

if __name__ == '__main__':
    sample_booleans = [True, False]
    print(truth_table(sample_booleans))