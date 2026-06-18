"""
Script to convert length from meters to feet.

This module provides a function to perform the conversion using 
the standard conversion factor (1 meter = 3.28084 feet).
It includes sample usage in the main block without interactive input.
"""

def meters_to_feet(meters: float) -> float:
    """
    Convert a length given in meters to its equivalent in feet.

    Args:
        meters (float): The length value in meters.

    Returns:
        float: The converted length in feet, rounded to 4 decimal places 
               for standard precision display purposes.
    
    Example:
        >>> meters_to_feet(1)
        3.2808
    
    Raises:
        TypeError: If the input is not a numeric type (int or float).
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be an integer or float representing meters.")

    # Conversion factor: 1 meter = 3.28084 feet
    conversion_factor = 3.28084
    
    return round(meters * conversion_factor, 4)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No interactive input is used here as per requirements.

    test_cases = [1, 5, 10, 25]

    print("Meters to Feet Conversion Results:")
    print("-" * 30)

    for meter_value in test_cases:
        feet_value = meters_to_feet(meter_value)
        # Formatting output clearly showing input and result separated by comma/space
        formatted_output = f"{meter_value} m, {feet_value:.4f} ft"
        print(formatted_output)

    # Additional sample calculation with a specific known value for verification context
    special_case_meters = 0.5
    feet_result = meters_to_feet(special_case_meters)
    print("-" * 30)
    print(f"Special check: {special_case_meters} m is equal to {feet_result:.4f} ft")