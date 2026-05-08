def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if any(conditions[i] and conditions[j]):
                return False
    return True
if __name__ == '__main__':
    test_case_1 = [[True], [False], [True]]
    print(f"Test Case 1: {check_mutual_exclusivity(test_case_1)}")
    test_case_2 = [[True], [True], [False]]
    print(f"Test Case 2: {check_mutual_exclusivity(test_case_2)}")
    test_case_3 = [[True], [False], [False]]
    print(f"Test Case 3: {check_mutual_exclusivity(test_case_3)}")
    test_case_4 = [[True, False], [False, True]]
    print(f"Test Case 4: {check_mutual_exclusivity(test_case_4)}")
    test_case_5 = [[True, True], [True, False]]
    print(f"Test Case 5: {check_mutual_exclusivity(test_case_5)}")
    test_case_6 = [[True], [True]]
    print(f"Test Case 6: {check_mutual_exclusivity(test_case_6)}")