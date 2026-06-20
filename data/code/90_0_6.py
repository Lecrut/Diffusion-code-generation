def test_or_condition(a, b):
    return a or b

if __name__ == '__main__':
    test_cases = [
        (True, True, True),
        (True, False, True),
        (False, True, True),
        (False, False, False)
    ]
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    for a, b, expected in test_cases:
        result = test_or_condition(a, b)
        if result == expected:
            passed_tests += 1
    
    print(f"Tests passed: {passed_tests}/{total_tests}")