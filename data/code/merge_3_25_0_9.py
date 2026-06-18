def is_zero(number):
    """
    Check if a given numeric input is exactly zero.

    Args:
        number (int | float): The numeric value to check.

    Returns:
        bool: True if number equals 0, False otherwise.
    """
    return number == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        0,
        -0,
        float(0),
        1,
        -5,
        3.14,
        -2.7e-9,  # Very small but not exactly zero in floating point context if treated as int comparison usually fails for non-zero floats unless explicitly checked, here we use == which works correctly for float(0) and others provided below
        
        0.0,
    ]

    results = []
    for value in test_cases:
        result = is_zero(value)
        print(f"Number: {value} (type: {type(value).__name__}) -> Is Zero? {result}")
        
        # Verify that float(0) works correctly with integer 0 and zero division edge cases if needed 
        # but the task strictly asks for "exactly zero", so standard equality check is robust.