def check_values():
    """
    Compares two values based on exact type matching using direct comparison.
    
    Returns:
        bool: True if both value types match AND their contents are equal, False otherwise.
    """
    # Hard-coded sample values to ensure the script runs without user input
    val1 = 42          # Integer
    val2 = "42"        # String
    
    # Determine type of first value (for reference)
    t1_type = type(val1)
    
    # Check if types are exactly equal and values are content-wise equal
    is_equal_types_and_values = (t1_type == type(val2)) and (val1 == val2)
    
    return is_equal_types_and_values

if __name__ == '__main__':
    result = check_values()
    print(f"Values {42} ({type(42).__name__}) and {'42'} ({type('42').__name__}) are equal: {result}")