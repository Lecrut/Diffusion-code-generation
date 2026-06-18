"""
Script to convert length from meters to feet.

This module provides a function to perform the conversion between metric 
and imperial units of length, specifically converting meters to feet.
The standard conversion factor is 1 meter = 3.28084 feet.

Author: AI Assistant
Date: October 26, 2023
"""

def convert_meters_to_feet(meters):
    """
    Converts a length given in meters to its equivalent in feet.

    Args:
        meters (float or int): The length value in meters.

    Returns:
        float: The converted length in feet, rounded to 6 decimal places 
               for standard precision representation.
    
    Raises:
        TypeError: If the input is not a numeric type suitable for conversion.
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be an integer or float representing meters.")

    # Conversion factor: 1 meter = 3.28084 feet
    FEET_PER_METER = 3.28084
    
    return round(meters * FEET_PER_METER, 6)

if __name__ == '__main__':
    # Sample test cases with hard-coded values as per requirements.
    
    sample_meters_1 = 5
    sample_meters_2 = 3.5
    
    feet_result_1 = convert_meters_to_feet(sample_meters_1)
    print(f"{sample_meters_1} meters is equal to {feet_result_1} feet.")

    feet_result_2 = convert_meters_to_feet(sample_meters_2)
    print(f"{sample_meters_2} meters is equal to {feet_result_2} feet.")