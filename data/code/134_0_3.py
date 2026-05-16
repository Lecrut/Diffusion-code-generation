def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if conditions[i] and conditions[j]:
                return False
    return True
if __name__ == '__main__':
    test_case_1 = [(True,), (False,), (True,)]
    result_1 = check_mutual_exclusivity(test_case_1)
    print(f"Test Case 1: {test_case_1}, Result: {result_1}")
    test_case_2 = [(True,), (True,), (False,)]
    result_2 = check_mutual_exclusivity(test_case_2)
    print(f"Test Case 2: {test_case_2}, Result: {result_2}")
    test_case_3 = [(True, True), (False, False)]
    result_3 = check_mutual_exclusivity(test_case_3)
    print(f"Test Case 3: {test_case_3}, Result: {result_3}")
    test_case_4 = [(True, True), (True, False)]
    result_4 = check_mutual_exclusivity(test_case_4)
    print(f"Test Case 4: {test_case_4}, Result: {result_4}")
    test_case_5 = [(True,), (True,)]
    result_5 = check_mutual_exclusivity(test_case_5)
    print(f"Test Case 5: {test_case_5}, Result: {result_5}")
    test_case_6 = [(False,), (False,)]
    result_6 = check_mutual_exclusivity(test_case_6)
    print(f"Test Case 6: {test_case_6}, Result: {result_6}")
    test_case_7 = [(True, True), (False, True), (True, False)]
    result_7 = check_mutual_exclusivity(test_case_7)
    print(f"Test Case 7: {test_case_7}, Result: {result_7}")