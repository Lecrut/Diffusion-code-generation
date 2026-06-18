#!/usr/bin/env python3
"""
Module to convert length from meters to feet.

This module provides a function to perform metric conversion 
specifically targeting the distance unit of meters (m) into feet (ft).

Usage:
    import meters_to_feet
    result = meters_to_feet.convert(10)  # Returns approximately 32.8084 ft
    
    if __name__ == '__main__':
        pass  # Run the module directly with sample data in this block
"""

def convert_meters_to_feet(meter_value: float) -> float:
    """
    Convert a length value from meters to feet.

    The conversion factor is based on the international definition where 
    one foot equals exactly 0.3048 meters, implying one meter equals approximately 
    1/0.3048 or about 3.28084 feet.

    Args:
        meter_value (float): The length in meters to be converted. Can be positive, zero, or negative.

    Returns:
        float: The equivalent length in feet, rounded to a reasonable precision 
              for standard calculations unless high precision is required downstream.
    
    Raises:
        TypeError: If the input 'meter_value' is not an instance of int or float.
        
    Example:
        >>> convert_meters_to_feet(1)
        3.28084
        
    """
    if not isinstance(meter_value, (int, float)):
        raise TypeError("Input must be a number representing meters.")

    # Conversion factor: 1 meter = 1/0.3048 feet ≈ 3.28084 ft
    return round(meter_value / 0.3048, 5)

if __name__ == '__main__':
    """Main execution block with hard-coded sample values."""

    # Sample test cases including edge cases like zero and negative numbers
    samples = [10, 2.5, 0, -5]

    print("Conversion from meters to feet:")
    for meter_val in samples:
        converted_feet = convert_meters_to_feet(meter_val)
        print(f"{meter_val} m is approximately {converted_feet} ft")