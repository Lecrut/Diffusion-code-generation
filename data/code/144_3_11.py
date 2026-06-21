def truth_table(booleans):
    from itertools import product
    return [[b for b in p] for p in product(*[[False, True]] * len(booleans))]

if __name__ == '__main__':
    print(truth_table([True, False]))