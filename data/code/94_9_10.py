def check_at_least_one(iterable):
    return any(iterable)

if __name__ == '__main__':
    TRUE_FLAG = True
    FALSE_FLAG = False

    test_case_1 = [FALSE_FLAG, FALSE_FLAG, FALSE_FLAG]
    test_case_2 = [TRUE_FLAG, FALSE_FLAG, FALSE_FLAG]
    test_case_3 = []
    test_case_4 = [0, FALSE_FLAG, None]
    test_case_5 = [1, 0, FALSE_FLAG]

    print(f"Test Case 1: {test_case_1} -> {check_at_least_one(test_case_1)}")
    print(f"Test Case 2: {test_case_2} -> {check_at_least_one(test_case_2)}")
    print(f"Test Case 3: {test_case_3} -> {check_at_least_one(test_case_3)}")
    print(f"Test Case 4: {test_case_4} -> {check_at_least_one(test_case_4)}")
    print(f"Test Case 5: {test_case_5} -> {check_at_least_one(test_case_5)}")