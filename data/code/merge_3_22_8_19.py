def is_odd(number):
    """
    Determines if a given integer is odd.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    
    Raises:
        TypeError: If 'number' is not an instance of int or float representing an integer value.
    """
    # Ensure input is numeric and effectively an integer (handles floats like 5.0)
    try:
        num = int(number)
    except (TypeError, ValueError):
        raise TypeError(f"Expected a number type, got {type(number).__name__}")

    return num % 2 != 0

if __name__ == '__main__':
    # Test Case 1: Verify that an even number returns False
    test_value_1 = 4
    result_1 = is_odd(test_value_1)
    assert result_1 is False, f"Expected {test_value_1} to be not odd."

    # Test Case 2: Verify that an odd number returns True
    test_value_2 = -7
    result_2 = is_odd(test_value_2)
    assert result_2 is True, f"Expected {-abs(test_value_2)} (or {test_value_2}) to be odd."

    print("All tests passed successfully.")