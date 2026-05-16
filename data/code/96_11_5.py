def evaluate_nested_logic(logic_structure):
    if isinstance(logic_structure, bool):
        return logic_structure
    elif isinstance(logic_structure, list) or isinstance(logic_structure, tuple):
        if not logic_structure:
            return False
        if len(logic_structure) == 1:
            return evaluate_nested_logic(logic_structure[0])
        if len(logic_structure) > 1:
            results = [evaluate_nested_logic(item) for item in logic_structure]
            if all(results):
                return True
            if any(results):
                return False
            return False
        return False
    return False
if __name__ == '__main__':
    test_case_1 = [True, True]
    test_case_2 = [False, True]
    test_case_3 = [True, False, True]
    test_case_4 = [False]
    test_case_5 = [True, True, True]
    test_case_6 = []
    test_case_7 = [False, False]
    test_case_8 = [True]
    test_case_9 = [False, True, False]
    print(f"Test Case 1: {evaluate_nested_logic(test_case_1)}")
    print(f"Test Case 2: {evaluate_nested_logic(test_case_2)}")
    print(f"Test Case 3: {evaluate_nested_logic(test_case_3)}")
    print(f"Test Case 4: {evaluate_nested_logic(test_case_4)}")
    print(f"Test Case 5: {evaluate_nested_logic(test_case_5)}")
    print(f"Test Case 6: {evaluate_nested_logic(test_case_6)}")
    print(f"Test Case 7: {evaluate_nested_logic(test_case_7)}")
    print(f"Test Case 8: {evaluate_nested_logic(test_case_8)}")
    print(f"Test Case 9: {evaluate_nested_logic(test_case_9)}")