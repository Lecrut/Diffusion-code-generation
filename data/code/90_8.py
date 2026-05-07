def simulate_boolean_logic(vars):
    results = {}
    for var_name, conditions in vars.items():
        result = False
        for condition in conditions:
            if condition:
                result = True
                break
        results[var_name] = result
    return results
def test_boolean_logic(vars, expected_results):
    actual_results = simulate_boolean_logic(vars)
    is_correct = actual_results == expected_results
    return is_correct, actual_results, expected_results
if __name__ == '__main__':
    variables = {
        "A": [True, False],
        "B": [False, True],
        "C": [True, True]
    }
    test_case_1_vars = variables
    test_case_1_expected = {
        "A": True,
        "B": True,
        "C": True
    }
    is_correct1, actual1, expected1 = test_boolean_logic(test_case_1_vars, test_case_1_expected)
    print(f"Test Case 1:")
    print(f"Correct: {is_correct1}")
    print(f"Actual: {actual1}")
    print(f"Expected: {expected1}\n")
    variables_2 = {
        "X": [False, False],
        "Y": [True, False]
    }
    test_case_2_vars = variables_2
    test_case_2_expected = {
        "X": False,
        "Y": True
    }
    is_correct2, actual2, expected2 = test_boolean_logic(test_case_2_vars, test_case_2_expected)
    print(f"Test Case 2:")
    print(f"Correct: {is_correct2}")
    print(f"Actual: {actual2}")
    print(f"Expected: {expected2}\n")
    variables_3 = {
        "P": [False],
        "Q": [False]
    }
    test_case_3_vars = variables_3
    test_case_3_expected = {
        "P": False,
        "Q": False
    }
    is_correct3, actual3, expected3 = test_boolean_logic(test_case_3_vars, test_case_3_expected)
    print(f"Test Case 3:")
    print(f"Correct: {is_correct3}")
    print(f"Actual: {actual3}")
    print(f"Expected: {expected3}\n")