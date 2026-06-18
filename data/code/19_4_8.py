def evaluate_inequality(x, y):
    """
    Checks if x is less than or equal to y.
    
    Args:
        x (any comparable type): The first value to compare.
        y (any comparable type): The second value to compare.
        
    Returns:
        bool: True if x <= y, False otherwise.
        
    Raises:
        TypeError: If either x or y cannot be compared directly.
    """
    try:
        return x <= y
    except TypeError as e:
        # Gracefully handle type errors by returning a default boolean indicating failure to compare
        raise ValueError(f"Cannot compare values of types {type(x)} and {type(y)}.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (5, 10),      # Should return True
        (10, 5),      # Should return False
        (3.14, 2.71),# Should return False
        ("apple", "banana"), # Should return True (string comparison)
        ([1], [2]),   # Should return True (list comparison)
    ]

    for i, (x_val, y_val) in enumerate(test_cases):
        try:
            result = evaluate_inequality(x_val, y_val)
            print(f"Test case {i+1}: x={repr(x_val)}, y={repr(y_val)} -> Result: {result}")
        except ValueError as ve:
            # This block catches the intentional error for incompatible types if any were added later
            print(f"Test case {i+1} raised an expected comparison error.")

    # Example with a potential type mismatch to demonstrate graceful handling logic (though it raises)
    try:
        result = evaluate_inequality(5, "ten")
    except ValueError as e:
        print(f"Demonstration of error handling for incompatible types:\n{e}")