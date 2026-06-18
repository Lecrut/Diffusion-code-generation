def is_even(number):
    """Check if a number is even."""
    return isinstance(number, (int, float)) and number % 2 == 0

if __name__ == '__main__':
    test_cases = [
        {"input": 0, "expected": True},
        {"input": -4, "expected": True},
        {"input": -3, "expected": False},
        {"input": 100, "expected": True},
        {"input": 7.5, "expected": False}
    ]

    for test in test_cases:
        result = is_even(test["input"])
        assert result == test["expected"], f"Failed for input {test['input']}: expected {test['expected']}, got {result}"
    
    print("All tests passed.")