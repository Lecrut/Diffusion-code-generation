def compare_temperatures(temp_a: float, temp_b: float) -> str:
    """
    Compares two temperature values and returns a string representation of their relationship.
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        str: "greater than" if A > B, "less than" if A < B, or "equal to" otherwise.
    """
    if temp_a > temp_b:
        return "greater than"
    elif temp_a < temp_b:
        return "less than"
    else:
        return "equal to"

if __name__ == '__main__':
    # Test Case 1: A is greater than B
    result = compare_temperatures(25.0, 20.0)
    assert result == "greater than", f"Expected 'greater than', got '{result}'"

    # Test Case 2: A is less than B
    result = compare_temperatures(-10.0, -5.0)
    assert result == "less than", f"Expected 'less than', got '{result}'"

    # Test Case 3: A is equal to B (including floats and integers acting as float)
    result = compare_temperatures(36.5, 36.5)
    assert result == "equal to", f"Expected 'equal to', got '{result}'"
    
    result = compare_temperatures(0, 0)
    assert result == "equal to", f"Expected 'equal to', got '{result}'"

    print("All tests passed successfully.")