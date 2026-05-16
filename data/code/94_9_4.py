def check_at_least_one(iterable):
    return any(iterable)
if __name__ == '__main__':
    test_case_1 = [False, False, False]
    test_case_2 = [False, True, False]
    test_case_3 = [None, False]
    test_case_4 = [1, 0, False]
    test_case_5 = []
    test_case_6 = [0, "", False]
    print(f"Test Case 1: {test_case_1} -> {check_at_least_one(test_case_1)}")
    print(f"Test Case 2: {test_case_2} -> {check_at_least_one(test_case_2)}")
    print(f"Test Case 3: {test_case_3} -> {check_at_least_one(test_case_3)}")
    print(f"Test Case 4: {test_case_4} -> {check_at_least_one(test_case_4)}")
    print(f"Test Case 5: {test_case_5} -> {check_at_least_one(test_case_5)}")
    print(f"Test Case 6: {test_case_6} -> {check_at_least_one(test_case_6)}")