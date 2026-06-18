def compare_temperature(value1: float, value2: float) -> str:
    """
    Compare two temperature values and return a descriptive string.
    
    Args:
        value1 (float): First temperature value in Celsius.
        value2 (float): Second temperature value in Celsius.
        
    Returns:
        str: A message indicating whether the first value is greater, 
             less than, or equal to the second value.
    """
    if value1 > value2:
        return f"{value1} is greater than {value2}"
    elif value1 < value2:
        return f"{value1} is less than {value2}"
    else:
        return f"{value1} is equal to {value2}"

if __name__ == '__main__':
    # Test case 1: Greater than condition
    assert compare_temperature(30.5, 25.0) == "30.5 is greater than 25.0", "Test 1 failed: Greater than"
    
    # Test case 2: Less than condition
    assert compare_temperature(-5.0, -9.5) == "-5.0 is less than -9.5", "Test 2 failed: Less than"

    # Test case 3: Equality condition
    assert compare_temperature(18.7, 18.7) == "18.7 is equal to 18.7", "Test 3 failed: Equality"
    
    print("All assertions passed successfully.")