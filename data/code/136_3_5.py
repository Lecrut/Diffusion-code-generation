def check_conditions(conditions):
    if not conditions:
        return True
    return all(conditions)
if __name__ == '__main__':
    test_case_1 = [True, True, False]
    result_1 = check_conditions(test_case_1)
    print(f"Test Case 1: {test_case_1}, Result: {result_1}")
    test_case_2 = [True, True, True]
    result_2 = check_conditions(test_case_2)
    print(f"Test Case 2: {test_case_2}, Result: {result_2}")
    test_case_3 = [False, True, False]
    result_3 = check_conditions(test_case_3)
    print(f"Test Case 3: {test_case_3}, Result: {result_3}")
    test_case_4 = []
    result_4 = check_conditions(test_case_4)
    print(f"Test Case 4: {test_case_4}, Result: {result_4}")
    test_case_5 = [True]
    result_5 = check_conditions(test_case_5)
    print(f"Test Case 5: {test_case_5}, Result: {result_5}")