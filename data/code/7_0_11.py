def convert_time(value: float | int, source_unit: str, target_unit: str) -> float:
    """
    Converts a time value from one unit (seconds, minutes, hours) to another.
    
    Args:
        value: The numeric time value to convert.
        source_unit: The original unit of the value ('s', 'm', or 'h').
        target_unit: The desired unit for conversion ('s', 'm', or 'h').
        
    Returns:
        The converted time as a float in the target unit.
        
    Raises:
        ValueError: If source_unit or target_unit is not one of 's', 'm', or 'h'.
    
    Examples (docstring only):
        convert_time(60, 's', 'm') -> 1.0
        convert_time(90, 'm', 'h') -> 1.5
        convert_time(3, 'h', 's') -> 10800.0
    
    Raises:
        ValueError: If the input units are invalid or mismatched in an unexpected way (though logic allows any pair).
    
    Note:
        This function handles conversions between seconds ('s'), minutes ('m'), and hours ('h').

    :param value: The numeric time value. Can be int or float.
    :type value: float | int
    :param source_unit: Source unit string, must be 's', 'm', or 'h'.
    :type source_unit: str
    :param target_unit: Target unit string, must be 's', 'm', or 'h'.
    :type target_unit: str
    :return: Converted time value as a float.
    :rtype: float
    
    """

    # Normalize input types to float for consistent calculation
    val = float(value)

    valid_units = {'s': 1, 'm': 60, 'h': 3600}
    
    if source_unit.lower() not in valid_units or target_unit.lower() not in valid_units:
        raise ValueError(f"Invalid unit provided. Use one of {list(valid_units.keys())}")

    # Convert value to seconds first (base unit), then convert to target unit
    base_seconds = val * valid_units[source_unit]
    
    factor_to_target = 1 / valid_units[target_unit]
    converted_value = base_seconds * factor_to_target
    
    return round(converted_value, 2)

if __name__ == '__main__':

    # Sample test cases to demonstrate functionality without user input or external dependencies
    print("Running time conversion tests...")
    
    # Convert 60 seconds to minutes
    result1 = convert_time(60, "s", "m")
    assert abs(result1 - 1.0) < 0.001
    
    # Convert 90 minutes to hours
    result2 = convert_time(90, "m", "h")
    assert abs(result2 - 1.5) < 0.001
    
    # Convert 3 hours to seconds
    result3 = convert_time(3, "h", "s")
    assert abs(result3 - 10800.0) == 0.0
    
    # Test fractional input: 45 minutes to seconds (should be 2700)
    result4 = convert_time(45.5, "m", "s")
    expected_result4 = round(45.5 * 60, 2)
    assert abs(result4 - expected_result4) < 0.1
    
    # Test edge case: zero value
    result5 = convert_time(0, "h", "s")
    assert result5 == 0.0

    print("All tests passed successfully.")