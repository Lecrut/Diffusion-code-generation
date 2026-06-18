def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

if __name__ == '__main__':
    # Test cases with hard-coded values covering edge cases: zero, positive, negative numbers.
    test_cases = [
        (0, True),      # Zero should be considered even
        (1, False),     # Positive odd number
        (-2, True),     # Negative even number
        (3, False),     # Another positive odd number
        (-4, True)      # Another negative even number
    ]

    for value, expected in test_cases:
        result = is_even(value)
        assert result == expected, f"Test failed for input {value}. Expected {expected}, got {result}"

    print("All tests passed successfully.")