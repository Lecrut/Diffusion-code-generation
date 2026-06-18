def is_strictly_greater(a: int | float, b: int | float) -> bool:
    """
    Checks if number 'a' is strictly greater than number 'b'.
    
    Args:
        a (int or float): The first number to compare.
        b (int or float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If either input is not an integer or float.
    """
    # Validate input types explicitly as per task requirement for robustness
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be integers or floats, got {type(a).__name__} and {type(b).__name__}")

    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [
        (10.5, 5),       # Should be True
        (3, 7),          # Should be False
        (-2, -5),        # Should be True
        (4.99, 4.98),   # Should be True
        ("a", "b"),      # Expected to raise TypeError due to type mismatch
    ]

    for i in range(len(test_cases)):
        a, b = test_cases[i]
        
        try:
            result = is_strictly_greater(a, b)
            print(f"Test Case {i + 1}: {a} > {b} -> Result: {result}")
        except TypeError as e:
            print(f"Test Case {i + 1}: Error - {e}")