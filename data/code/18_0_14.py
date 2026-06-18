def is_strictly_greater(a: float | int, b: float | int) -> bool:
    """
    Check if number a is strictly greater than number b.
    
    Args:
        a (float|int): The first number to compare.
        b (float|int): The second number to compare against.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If either input is not an integer or float.
    """
    # Validate input types strictly as per requirement for robustness without external libs
    valid_types = (int, float)
    
    if not isinstance(a, valid_types):
        raise TypeError(f"Expected numeric type but got {type(a).__name__} for 'a'")
    if not isinstance(b, valid_types):
        raise TypeError(f"Expected numeric type but got {type(b).__name__} for 'b'")
    
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        (10, 5),      # Should be True
        (3.5, 2.1),   # Should be True
        (7, 7),       # Should be False (not strictly greater)
        (-1, -5),     # Should be True
    ]
    
    for val_a, val_b in test_cases:
        try:
            result = is_strictly_greater(val_a, val_b)
            print(f"is_strictly_greater({val_a}, {val_b}) = {result}")
        except TypeError as e:
            # This block handles potential type errors if inputs were malformed strings later
            print(f"Error with input types for ({val_a}, {val_b}): {e}")