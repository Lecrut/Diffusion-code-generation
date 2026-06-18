def compare_values():
    """
    Compares two values based on exact type matching using direct comparison.
    Returns True if both value and type match, False otherwise.
    
    Parameters:
        val1 (any): First value to compare.
        val2 (any): Second value to compare.
        
    Returns:
        bool: True if val1 == val2 AND type(val1) is same as type(val2), else False.
    """
    return val1 == val2 and type(val1) is type(val2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    a = 5
    b = "5"

    result = compare_values(a, b)
    
    print(f"{a} and {b}: Type match? False")