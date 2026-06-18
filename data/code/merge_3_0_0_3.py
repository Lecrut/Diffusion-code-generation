"""
Module to convert length from meters to feet.

This module provides a function to convert a distance given in meters 
to its equivalent value in feet using the standard conversion factor.
1 meter is approximately equal to 3.28084 feet.
"""

def meters_to_feet(meters: float) -> float:
    """
    Convert a length from meters to feet.

    Args:
        meters (float): The length in meters. Must be non-negative.

    Returns:
        float: The equivalent length in feet, rounded to 4 decimal places 
              for standard precision representation.

    Raises:
        ValueError: If the input 'meters' is negative.
    
    Example:
        >>> meters_to_feet(1)
        3.2808
    
    Note:
        The conversion factor used is exactly 39 inches per meter (since 
        there are 1574.8 inches in a mile and 63,360 inches in a statute mile).
        However, the standard approximation of 3.28084 feet/meter is widely accepted.
    """
    if meters < 0:
        raise ValueError("Length cannot be negative.")

    # Conversion factor: 1 meter = 3.28084 feet
    conversion_factor = 3.28084
    
    return round(meters * conversion_factor, 4)

if __name__ == '__main__':
    # Hard-coded sample values for testing the function without interactive input
    test_cases = [1, 5, 10, 100]

    print("Meters to Feet Conversion Results:")
    print("-" * 30)
    
    for meter_value in test_cases:
        feet_value = meters_to_feet(meter_value)
        print(f"{meter_value} m is equal to {feet_value} ft")