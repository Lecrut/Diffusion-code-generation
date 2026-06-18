def compare_values(val1, val2):
    """
    Compares two values to determine if they are equal.
    
    Args:
        val1 (any): The first value to compare.
        val2 (any): The second value to compare.
        
    Returns:
        bool: True if the values are equal, False otherwise.
    """
    try:
        return val1 == val2
    except TypeError as e:
        # Handles cases where types cannot be compared directly in some contexts,
        # though Python's '==' is generally robust for common built-in types.
        print(f"Error: Cannot compare these values - {e}")
        raise

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    value_a = 10
    value_b = "10"
    
    result = compare_values(value_a, value_b)
    
    if result:
        print(f"The inputs {value_a} and {value_b} are equal.")
    else:
        print(f"The inputs {value_a} and {value_b} are not equal.")