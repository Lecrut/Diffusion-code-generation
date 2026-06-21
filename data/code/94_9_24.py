def check_any_true(iterable):
    true_map = {True: True, False: False}
    for val in iterable:
        if true_map.get(val, False):
            return True
    return False

if __name__ == '__main__':
    cases = [
        [False, False, False],
        [False, True, False],
        [],
        [True],
        [False, False, True, False]
    ]
    for case in cases:
        print(check_any_true(case))