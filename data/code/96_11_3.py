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
            return any(results)
        return False
    else:
        return False
if __name__ == '__main__':
    test_case_1 = [True, True]
    test_case_2 = [False, True]
    test_case_3 = [True, False]
    test_case_4 = [False]
    test_case_5 = [True, True, False]
    test_case_6 = [False, False]
    test_case_7 = [True, True, True]
    test_case_8 = []
    test_case_9 = [True]
    test_case_10 = [False, False, False]
    print(f"Test 1: {evaluate_nested_logic(test_case_1)}")
    print(f"Test 2: {evaluate_nested_logic(test_case_2)}")
    print(f"Test 3: {evaluate_nested_logic(test_case_3)}")
    print(f"Test 4: {evaluate_nested_logic(test_case_4)}")
    print(f"Test 5: {evaluate_nested_logic(test_case_5)}")
    print(f"Test 6: {evaluate_nested_logic(test_case_6)}")
    print(f"Test 7: {evaluate_nested_logic(test_case_7)}")
    print(f"Test 8: {evaluate_nested_logic(test_case_8)}")
    print(f"Test 9: {evaluate_nested_logic(test_case_9)}")
    print(f"Test 10: {evaluate_nested_logic(test_case_10)}")