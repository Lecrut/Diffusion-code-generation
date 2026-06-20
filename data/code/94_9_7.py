def check_at_least_one(iterable):
    return any(iterable)

if __name__ == '__main__':
    test_case_1 = [False, False, False]
    test_case_2 = [True, False, False]
    result_1 = check_at_least_one(test_case_1)
    result_2 = check_at_least_one(test_case_2)
    print(f"Test Case 1: {test_case_1} -> {result_1}")
    print(f"Test Case 2: {test_case_2} -> {result_2}")