def test_or_condition(a, b):
    return a or b

if __name__ == '__main__':
    TEST_CASES = [
        (True, True, True),
        (True, False, True),
        (False, True, True),
        (False, False, False)
    ]
    
    all_passed = True
    for a, b, expected in TEST_CASES:
        result = test_or_condition(a, b)
        if result != expected:
            print(f"Test failed for a={a}, b={b}. Expected: {expected}, Got: {result}")
            all_passed = False
    
    if all_passed:
        print("All tests passed.")