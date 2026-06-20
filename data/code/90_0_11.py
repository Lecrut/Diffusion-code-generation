def test_or_condition(a, b):
    return a or b

if __name__ == '__main__':
    test_cases = [
        (True, True, True),
        (True, False, True),
        (False, True, True),
        (False, False, False)
    ]
    all_passed = True
    for a, b, expected in test_cases:
        result = test_or_condition(a, b)
        if result != expected:
            print(f"Test failed for a={a}, b={b}. Expected: {expected}, Got: {result}")