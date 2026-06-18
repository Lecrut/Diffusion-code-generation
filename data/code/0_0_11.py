import math

def meters_to_feet(meters: float) -> float:
    """
    Convert a length given in meters to feet.
    
    The conversion factor is 1 meter = 3.28084 feet (approximately).
    This constant is derived from the exact definition where 1 foot = 0.3048 meters exactly,
    so feet = meters / 0.3048 or equivalently meters * (1/0.3048).

    Args:
        meters (float): The length in meters to be converted. Must be a non-negative number 
                       representing distance; however, negative values are mathematically valid 
                       for the formula even if physically nonsensical without context.

    Returns:
        float: The equivalent length in feet.

    Raises:
        TypeError: If 'meters' is not an instance of int or float.
    
    Examples:
        >>> meters_to_feet(1)
        3.28084
        >>> meters_to.feet(0)
        0.0
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be a numeric value.")

    # Using the exact conversion factor: 1 foot = 0.3048 meters exactly.
    feet_per_meter = 1 / 0.3048
    
    return round(meters * feet_per_meter, 2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values as per task requirements.
    
    sample_inputs = [
        (1.6, "Height of a typical adult"),
        (3048, "Length of one mile in meters converted to feet"),
        (-5, "Negative value for mathematical demonstration")
    ]

    print("Meters to Feet Conversion Results:")
    print("-" * 30)
    
    for input_val, description in sample_inputs:
        try:
            result = meters_to_feet(input_val)
            print(f"{description}: {input_val} m -> {result} ft")
        except TypeError as e:
            print(f"Error processing {input_val}: {e}")

    # Additional specific test case for zero
    zero_result = meters_to_feet(0.0)
    assert zero_result == 0.0, "Zero meters should result in zero feet."
    
    # Specific value check: 1 meter is approximately 3.28 feet
    one_meter_result = meters_to_feet(1.0)
    expected_approx_1m_ft = round((1/0.3048), 2)
    assert abs(one_meter_result - expected_approx_1m_ft) < 0.01, "Conversion accuracy check failed."

    print("-" * 30)
    print("All sample conversions and internal assertions completed successfully.")