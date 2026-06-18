"""
Module to convert length from meters to feet.

This module provides a function to perform unit conversion between 
meters (SI base unit of length) and feet (Imperial/US Customary unit).
Conversion factor: 1 meter = approximately 3.28084 feet.
"""

def meters_to_feet(meters):
    """
    Convert a distance given in meters to its equivalent in feet.

    Args:
        meters (float or int): The length value in meters. Must be non-negative 
                              for physical distances, though the function will 
                              process negative numbers mathematically if needed.

    Returns:
        float: The converted length in feet. Rounded to 6 decimal places 
               for standard precision representation.

    Example:
        >>> meters_to_feet(1)
        3.28084
    """
    conversion_factor = 3.28084
    return round(meters * conversion_factor, 6)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No interactive input is used as per requirements.

    # Sample test cases covering various scenarios:
    samples = [1, 0, -5] 

    print("Meters to Feet Conversion Results:")
    print("-" * 30)

    for meter_value in samples:
        feet_value = meters_to_feet(meter_value)
        print(f"{meter_value} m is equal to {feet_value} ft")