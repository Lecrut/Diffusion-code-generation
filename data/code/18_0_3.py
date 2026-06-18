def is_strictly_greater(a: float, b: float) -> bool:
    """
    Check if number 'a' is strictly greater than number 'b'.
    
    Parameters:
        a (float): The first numeric value to compare.
        b (float): The second numeric value to compare against.
        
    Returns:
        bool: True if a > b, otherwise False.
        
    Raises:
        TypeError: If either input is not an instance of int or float.
    """
    # Validate input types strictly as per requirement for robustness without external prompts
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numbers (int or float). Got {type(a).__name__} and {type(b).__name__}.")
    
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line args, network access, or pre-existing files.
    
    test_cases = [
        (10, 5),      # Should be True
        (3.14, 2.71), # Should be True
        (-1, -5),     # Should be False (-1 is not greater than -5)
        (0, 0),       # Should be False (equal values are not strictly greater)
    ]

    for val_a, val_b in test_cases:
        try:
            result = is_strictly_greater(val_a, val_b)
            print(f"is_strictly_greater({val_a}, {val_b}) -> {result}")
        except TypeError as e:
            # Graceful handling of potential type errors during the hard-coded execution
            print(f"Error for inputs ({val_a}, {val_b}): {e}")