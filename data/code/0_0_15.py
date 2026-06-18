"""
Module: meters_to_feet_converter

This module provides functionality to convert a length value from meters to feet.

Conversion factor used: 1 meter = 3.28084 feet (standard international conversion).
The function performs the multiplication of the input meters by this constant.

Author: AI Assistant
Date: October 26, 2023
"""

def convert_meters_to_feet(meters: float) -> float:
    """
    Converts a length given in meters to feet.

    Args:
        meters (float): The length value in meters. Must be non-negative for physical lengths, 
                        though the function mathematically works with negative values too.

    Returns:
        float: The equivalent length in feet. Rounded to 4 decimal places for readability.

    Raises:
        TypeError: If 'meters' is not a numeric type (int or float).
    
    Example:
        >>> convert_meters_to_feet(1)
        3.2808
    
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be an integer or float representing meters.")

    # Standard conversion factor: 1 meter = 3.28084 feet
    FEET_PER_METER = 3.28084
    
    return round(meters * FEET_PER_METER, 4)

if __name__ == '__main__':
    """
    Main execution block containing hard-coded sample values for testing the conversion function.
    No interactive input is used here as per task requirements.
    
    Sample cases cover:
        - A standard room length (3 meters)
        - An athlete's sprint distance (100 meters)
        - Zero meters
    
    """

    # Define sample meter values to test the conversion function
    SAMPLE_METERS = [3, 100.5, 0]

    print("Meters to Feet Conversion Results")
    print("-" * 25)

    for value in SAMPLE_METERS:
        feet_value = convert_meters_to_feet(value)
        # Print formatted output showing input and converted result
        print(f"{value} meters is equal to {feet_value} feet.")