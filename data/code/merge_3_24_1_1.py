def is_negative(value):
    """Check if a number is negative."""
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values
    test_cases = [
        -5,   # Should be True
        -3.14,  # Should be True
        0,     # Should be False (zero is not negative)
        7,      # Should be False
        float('-inf'),  # Edge case: should be True
    ]

    for num in test_cases:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")