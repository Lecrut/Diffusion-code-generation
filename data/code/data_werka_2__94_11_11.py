def check_any_true(values):
    truth_map = {True: 1, False: 0}
    total = sum(truth_map.get(v, 0) for v in values)
    return total > 0

if __name__ == '__main__':
    test_list = [False, False, True, False]
    print(check_any_true(test_list))