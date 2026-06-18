"""
Module to convert length from meters to feet.

This module provides a function to perform the conversion between 
meters (SI unit of length) and feet (Imperial/US Customary unit).
The conversion factor is approximately 3.28084 feet per meter.
"""

def meters_to_feet(meters: float) -> float:
    """
    Convert a distance given in meters to its equivalent in feet.

    Args:
        meters (float): The length value in meters. Must be non-negative 
                       for physical distances, though the function will 
                       return negative results if input is negative.

    Returns:
        float: The converted length in feet.

    Example:
        >>> print(meters_to_feet(1))
        3.28084
    """
    # Conversion factor: 1 meter = 3.28084 feet (approximate)
    FEET_PER_METER = 3.28084
    
    return meters * FEET_PER_METER

if __name__ == '__main__':
    # Hard-coded sample values for testing the conversion function.
    
    # Sample input: Convert standard human height (~1.75m) to feet
    sample_height_meters = 1.75
    
    result_feet = meters_to_feet(sample_height_meters)
    
    print(f"{sample_height_meters} meters is equal to {result_feet:.2f} feet.")

    # Additional test case: Convert a standard car length (~4m) 
    sample_car_length_meters = 4.0
    
    result_car_feet = meters_to_feet(sample_car_length_meters)
    
    print(f"{sample_car_length_meters} meters is equal to {result_car_feet:.2f} feet.")