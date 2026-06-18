def compare_temperature(temp1: float, temp2: float) -> int:
    """
    Compares two temperature values and returns an integer result.
    
    Returns:
        1 if temp1 is greater than temp2
       -1 if temp1 is less than temp2
         0 if they are equal
    
    Raises:
        TypeError: If inputs are not numeric (int or float)
    """
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    
    return 1 if temp1 > temp2 else (-1 if temp1 < temp2 else 0)

if __name__ == '__main__':
    # Test case: Greater than
    result = compare_temperature(35.6, 20.0)
    assert result == 1, "Failed assertion for greater than comparison."

    # Test case: Less than
    result = compare_temperature(19.4, 25.8)
    assert result == -1, "Failed assertion for less than comparison."

    # Test case: Equality
    temp_a = 0.0
    temp_b = float(temp_a)
    result = compare_temperature(temp_a, temp_b)
    assert result == 0, "Failed assertion for equality comparison."

    print("All tests passed successfully.")