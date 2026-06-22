def check_existence(data_list):
    if not data_list:
        return False
    return any(data_list)

if __name__ == '__main__':
    test_cases = {
        "empty": [],
        "all_false": [False, False, False],
        "mixed": [False, True, False],
        "all_true": [True, True],
        "single_true": [True],
        "single_false": [False],
    }
    for name, values in test_cases.items():
        result = check_existence(values)
        print(f"{name}: {result}")