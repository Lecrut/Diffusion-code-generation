def is_even(number):
    """Check if a number is even."""
    return isinstance(number, (int, float)) and number % 2 == 0

if __name__ == '__main__':
    test_cases = [
        {"input": 0, "expected": True},
        {"input": -4, "expected": True},
        {"input": 3, "expected": False},
        {"input": -7.5, "expected": False},
        {"input": float("inf"), "expected": False},
    ]

    for case in test_cases:
        result = is_even(case["input"])
        assert result == case["expected"], f"Failed for input {case['input']}: expected {case['expected']}, got {result}"

    print("All tests passed.")