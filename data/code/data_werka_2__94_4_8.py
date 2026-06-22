def check_existence(data_list):
    if not data_list:
        return False
    return any(data_list)

if __name__ == '__main__':
    tests = {
        "empty": [],
        "all_false": [False, False, False],
        "one_true": [False, True, False],
        "all_true": [True, True],
        "single_true": [True],
        "single_false": [False]
    }
    for name, val in tests.items():
        print(check_existence(val))