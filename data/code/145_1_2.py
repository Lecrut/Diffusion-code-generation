def test_nested_logic(test_cases):
    results = {}
    for name, (expected, actual) in test_cases.items():
        results[name] = {"expected": expected, "actual": actual}
    return results
if __name__ == '__main__':
    test_data = {
        "case_1": (True, True),
        "case_2": (False, False),
        "case_3": (True, False),
        "case_4": (False, True),
        "case_5": (True, True)
    }
    results = test_nested_logic(test_data)
    print(results)