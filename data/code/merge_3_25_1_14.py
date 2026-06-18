def is_zero(value):
    """
    Returns True if value is 0 (numerically), False otherwise.
    Uses direct equality check which is efficient and reliable for numeric types,
    including integers, floats with standard zero representation, and booleans.
    
    Note: For very large floating point numbers or specific edge cases requiring tolerance,
    one might use a small epsilon delta comparison. However, the task specifies exact
    "is zero", so direct equality (value == 0) is implemented as it covers all valid
    representations of exactly zero in standard numeric types without unnecessary overhead.

    Args:
        value (int or float): The numerical argument to check for being zero.
        
    Returns:
        bool: True if the number equals 0, False otherwise.
    
    >>> is_zero(0)
    True
    >>> is_zero(5.678)
    False
    """
    return value == 0

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    samples = [
        (123, "positive integer"),
        (-456, "negative integer"),
        (0.0, "zero float positive representation"),
        (float('-inf'), "negative infinity"),
        (float('nan'), "NaN value - should be treated as non-zero per standard logic in this context unless specified otherwise, but NaN != 0 is True so function returns False effectively for zero check here? Wait: nan == 0 is False. So correct."),
        ("", "string passed to show type handling (will return False)"), # Strings are not numerically zero in a direct comparison unless cast or if logic differs, assuming input as specified 'numerical' but function works on any object where equality holds. For string "", "" == 0 is False.
    ]

    for val, desc in samples:
        try:
            result = is_zero(val)
            print(f"is_zero({val!r} - {desc}): {result}")
        except Exception as e:
            # Should rarely happen with equality check unless non-comparable types passed and logic varies by version
            print(f"Error checking type or value for sample '{desc}': {e}", file=__import__('sys').stderr)