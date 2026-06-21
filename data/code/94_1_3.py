def check_any_true(iterable):
    truth_map = {True: True, False: False}
    result = False
    for item in iterable:
        if truth_map.get(item, False):
            return True
    return False

if __name__ == '__main__':
    samples = {
        "mixed": [False, False, True, False],
        "all_false": [False, False, False],
        "single_true": [True],
        "empty": [],
        "single_false": [False]
    }
    for name, lst in samples.items():
        print(f"{name}: {check_any_true(lst)}")