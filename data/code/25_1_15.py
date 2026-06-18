def is_zero(value):
    """
    Returns True if value is zero, False otherwise.
    Uses direct equality comparison which is efficient for numerical types in Python.
    
    Args:
        value (int | float | complex): The number to check
        
    Returns:
        bool: True if value equals 0, False otherwise
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (0.0, True),       # Float zero
        (-0.0, True),      # Negative float zero
        (int(0), True),    # Integer zero
        (1, False),        # Positive integer
        (-1, False),       # Negative integer
        (3.14, False),     # Non-zero float
        (complex(0, 0), True),   # Complex zero
        (complex(1, 2), False)    # Non-zero complex
    ]

    for num, expected in test_cases:
        result = is_zero(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"is_zero({num!r}) -> {result} (Expected: {expected}) [{status}]")