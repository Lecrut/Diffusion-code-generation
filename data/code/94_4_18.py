def check_existence(data_list):
    if data_list is None or len(data_list) == 0:
        return False
    for val in data_list:
        if val is True:
            return True
    return False

if __name__ == '__main__':
    test_cases = [
        [True, False, False],
        [False, False, False],
        [],
        [False, True],
        [None, None],
        [False]
    ]
    results = [check_existence(tc) for tc in test_cases]
    for i, res in enumerate(results):
        print(f"Case {i}: {res}")