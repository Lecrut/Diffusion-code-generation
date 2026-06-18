def determine_larger(value1: any = None, value2: any = None) -> any:
    """
    Returns the larger of two comparable values (integers or floats).
    
    Args:
        value1: The first comparable value.
        value2: The second comparable value.
        
    Returns:
        The greater of the two input values.
        
    Raises:
        TypeError: If either argument is not a numeric type and cannot be compared.
    """
    if isinstance(value1, (int, float)) or isinstance(value2, (int, float)):
        return value1 > value2 and value1 or value2
    
if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_int = determine_larger(50, 75)
    result_float = determine_larger(3.14, 99.876)
    
    print(f"Larger of integers: {result_int}")
    print(f"Larger of floats: {result_float}")