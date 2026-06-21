def truth_table(booleans):
    from itertools import product
    return [list(x) + [all(x)] for x in product(*[[False, True]] * len(booleans))]

if __name__ == '__main__':
    print(truth_table([True, False]))