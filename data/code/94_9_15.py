def check_at_least_one(iterable):
    return any(iterable)

if __name__ == '__main__':
    test_cases = {
        "test_case_1": [False, False, False],
        "test_case_2": [True, False, False],
        "test_case_3": [],
        "test_case_4": [0, False, None],
        "test_case_5": [1, 0, False]
    }
    
    for test_name, test_case in test_cases.items():
        result = check_at_least_one(test_case)
        print(f"{test_name}: {result}")