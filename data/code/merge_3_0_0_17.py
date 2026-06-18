"""
Module to convert length from meters to feet.

This script defines a function that takes a distance in meters as input 
and returns the equivalent distance in feet using the standard conversion factor: 1 meter = 3.28084 feet.

Usage Example:
    python convert_meters_to_feet.py
"""

def meters_to_feet(meters: float) -> float:
    """
    Convert a length value from meters to feet.

    Args:
        meters (float): The distance in meters.

    Returns:
        float: The equivalent distance in feet, rounded to 6 decimal places for precision without excessive digits.

    Raises:
        TypeError: If the input is not numeric.
    
    Example:
        >>> meters_to_feet(1)
        3.28084
    """
    if isinstance(meters, (int, float)):
        conversion_factor = 3.28084
        return round(meters * conversion_factor, 6)
    else:
        raise TypeError("Input must be a numeric value.")

if __name__ == '__main__':
    # Hard-coded sample values for testing the function directly without user input
    
    test_cases = [1.0, 25.4, 100.0]

    print(f"Meters to Feet Conversion Results:")
    
    for meter_value in test_cases:
        feet_value = meters_to_feet(meter_value)
        print(f"{meter_value} meters is equal to {feet_value} feet.")