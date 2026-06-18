def is_zero_value(s: str) -> bool:
    """
    Attempts to evaluate a user-provided string as a number.
    Returns True if and only if the numeric value is zero.
    
    Args:
        s (str): The input string to evaluate.
        
    Returns:
        bool: True if the parsed number is 0, False otherwise or on invalid input.
    """
    try:
        # Attempt to convert the string to a float first for broader support (e.g., "0", "-0")
        numeric_value = float(s)
        
        # Check if the value is numerically zero
        return numeric_value == 0.0
    except ValueError:
        # This block catches cases where 's' cannot be converted to a number
        pass
    
    # If any exception occurs or no conversion was successful, it returns False
    return False

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [
        "0",           # Should return True (zero)
        "-0.0",        # Should return True (negative zero is equal to positive zero in float comparison)
        "123",         # Should return False (non-zero integer)
        "abc",         # Should return False (invalid string, caught by try-except)
        "",            # Should return False (empty string raises ValueError)
    ]

    for test_input in test_cases:
        result = is_zero_value(test_input)
        print(f"Input '{test_input}' -> {result}")