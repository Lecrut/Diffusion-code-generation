def is_even(n):
    """Check if a number n is even."""
    return isinstance(n, (int, float)) and not isinstance(n, bool) and n % 2 == 0

if __name__ == '__main__':
    test_cases = [
        {"input": 0, "expected": True},
        {"input": -18, "expected": True},
        {"input": 7, "expected": False},
        {"input": -3.5, "expected": False},
        {"input": float("inf"), "expected": False},
    ]

    all_passed = True
    for case in test_cases:
        result = is_even(case["input"])
        passed = result == case["expected"]
        if not passed:
            print(f"Test failed for input {case['input']}: expected {case['expected']}, got {result}")
            all_passed = False

    if all_passed:
        print("All tests passed.")