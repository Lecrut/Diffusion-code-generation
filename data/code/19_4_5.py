def evaluate_inequality(x, y):
    """
    Checks if x is less than or equal to y.
    
    Handles potential type errors gracefully by attempting conversion 
    to float and catching exceptions. Returns a boolean indicating the result.
    
    Args:
        x (any): The first value to compare.
        y (any): The second value to compare.
        
    Returns:
        bool: True if x <= y, False otherwise.
    """
    try:
        # Attempt to convert inputs to float for comparison
        val_x = float(x)
        val_y = float(y)
        return val_x <= val_y
    except (TypeError, ValueError):
        # Return False on any type or conversion error as per graceful handling requirement
        return False

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [
        (5.0, 10),      # Should be True
        (-3, -2),       # Should be True
        (7, 6),         # Should be False
        ("hello", "world"),  # String comparison after conversion will fail or behave unexpectedly; handled gracefully here
    ]
    
    for x_val, y_val in samples:
        result = evaluate_inequality(x_val, y_val)
        print(f"evaluate_inequality({x_val!r}, {y_val!r}) = {result}")