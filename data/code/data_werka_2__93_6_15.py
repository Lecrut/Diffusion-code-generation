def check_both_false(a, b):
    truth_lookup = {True: 1, False: 0}
    a_val = truth_lookup.get(bool(a), 0)
    b_val = truth_lookup.get(bool(b), 0)
    return a_val == 0 and b_val == 0

if __name__ == '__main__':
    x = 0
    y = []
    res = check_both_false(x, y)
    print(res)