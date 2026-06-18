"""
Module to convert length from meters to feet.

This module provides a function to perform unit conversion between 
meters (SI base unit of length) and feet (Imperial/US Customary unit).
Conversion factor: 1 meter = 3.28084 feet.
"""

def meters_to_feet(meters: float) -> float:
    """
    Convert a length value from meters to feet.

    Args:
        meters (float): The length in meters to be converted. Must be non-negative 
                        if representing physical distance, though the function will 
                        process negative numbers mathematically as well.

    Returns:
        float: The equivalent length in feet.

    Example:
        >>> result = meters_to_feet(1)
        >>> print(result)  # Output approx 3.28084
    """
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No interactive input is used as per requirements.

    sample_meters_1 = 5.0
    sample_meters_2 = 10.5
    
    converted_feet_1 = meters_to_feet(sample_meters_1)
    converted_feet_2 = meters_to_feet(sample_meters_2)

    print(f"{sample_meters_1} meters is equal to {converted_feet_1:.4f} feet.")
    print(f"{sample_meters_2} meters is equal to {converted_feet_2:.4f} feet.")