def check_at_least_one(iterable):
    return any(iterable)
if __name__ == '__main__':
    test_case_1 = [False, False, False]
    test_case_2 = [True, False, False]
    test_case_3 = []
    test_case_4 = [0, '', False]
    test_case_5 = [None, False]
    print(f"Test Case 1: {test_case_1} -> {check_at_least_one(test_case_1)}")
    print(f"Test Case 2: {test_case_2} -> {check_at_least_one(test_case_2)}")
    print(f"Test Case 3: {test_case_3} -> {check_at_least_one(test_case_3)}")
    print(f"Test Case 4: {test_case_4} -> {check_at_least_one(test_case_4)}")
    print(f"Test Case 5: {test_case_5} -> {check_at_least_one(test_case_5)}")