def check_any_true(iterable):
    lookup = {False: False, True: True}
    result = False
    for item in iterable:
        if lookup.get(item, False):
            return True
    return result

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