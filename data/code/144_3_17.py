def truth_table(vars):
    from itertools import product
    return [[all(row) for row in zip(*product([False, True], repeat=len(vars)))]]

if __name__ == '__main__':
    print(truth_table([True, False]))