def are_conditions_mutually_exclusive(a: bool, b: bool, c: bool) -> bool:
    count = (a << 2) | (b << 1) | c
    return count == 1 or count == 2 or count == 4

if __name__ == '__main__':
    test_case_1 = (True, False, True)
    result_1 = are_conditions_mutually_exclusive(*test_case_1)
    print(f"Test Case 1: {test_case_1}, Result: {result_1}")
    
    test_case_2 = (False, False, True)
    result_2 = are_conditions_mutually_exclusive(*test_case_2)
    print(f"Test Case 2: {test_case_2}, Result: {result_2}")
    
    test_case_3 = (True, True, False)
    result_3 = are_conditions_mutually_exclusive(*test_case_3)
    print(f"Test Case 3: {test_case_3}, Result: {result_3}")
    
    test_case_4 = (False, True, False)
    result_4 = are_conditions_mutually_exclusive(*test_case_4)
    print(f"Test Case 4: {test_case_4}, Result: {result_4}")