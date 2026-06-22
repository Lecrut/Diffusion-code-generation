def check_both_false(a, b):
    truth_lookup = {0: 0, 1: 1, None: 0, True: 1, False: 0}
    a_bool = truth_lookup.get(a, int(bool(a)))
    b_bool = truth_lookup.get(b, int(bool(b)))
    return a_bool == 0 and b_bool == 0

if __name__ == '__main__':
    a = 0
    b = []
    result = check_both_false(a, b)
    print(result)