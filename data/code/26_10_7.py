def is_greater(a: float, b: float) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise returns False.

    Args:
        a (float): The first numerical value to compare.
        b (float): The second numerical value to compare against.

    Returns:
        bool: True if a > b, False otherwise.
    
    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(2, 7)
        False
        >>> is_greater(-10, -20)
        True

    Note:
        This function performs a direct comparison and raises no exceptions for 
        standard numerical types (int, float). It does not handle non-numeric inputs.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    test_cases = [
        ((10, 5), True),      # Positive integers: 10 > 5 is true
        (-3, -6),            # Negative numbers: -3 > -6 is true
        (4.2, 4.2),          # Equal floats should return false
        (float('inf'), float('-inf')), # Infinity cases: infinity > negative infinity is true
    ]

    for i, ((a_val, b_val), expected) in enumerate(test_cases):
        result = is_greater(a_val, b_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: is_greater({a_val}, {b_val})")
        print(f"Expected: {expected}")
        print(f"Got:      {result} -> {status}\n")