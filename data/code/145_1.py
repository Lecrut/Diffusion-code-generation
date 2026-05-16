def test_nested_logic(test_cases):
    results = {}
    for name, (expected, actual) in test_cases.items():
        results[name] = {"expected": expected, "actual": actual}
    return results
if __name__ == '__main__':
    test_data = {
        "case1": (True, True),
        "case2": (False, False),
        "case3": (True, False),
        "case4": (False, True),
        "case5": (True, True)
    }
    results = test_nested_logic(test_data)
    print(results)