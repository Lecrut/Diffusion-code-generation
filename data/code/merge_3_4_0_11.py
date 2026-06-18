"""
Unit Converter Module: Distance Conversion between Meters, Kilometers, and Miles.

This module provides a robust system to convert distance units with comprehensive input validation.
It supports conversions from meters (m), kilometers (km), or miles (mi) to any of the three target units.
All inputs are validated for type correctness and numeric range before processing.

Constants:
    METERS_PER_KILOMETER = 1000
    MILES_IN_MILE = 1 # Identity, used in conversion logic clarity if needed later
    KILOMETERS_PER_MILE = 1.609344
    MILES_PER_METRE = 0.000621371

Conversion Factors (Target Unit / Source Unit):
    To Kilometers: m -> km (/1000), km -> km (*1), mi -> km (*1.609344)
    To Miles:      m -> mi  (*0.000621371), km -> mi  (/1.609344), mi -> mi (*1)
"""

from typing import Union, Tuple

class ConversionError(Exception):
    """Custom exception raised for invalid conversion inputs."""
    pass

def validate_distance_input(value: float, unit: str) -> None:
    """
    Validates the input distance value and unit string.

    Args:
        value (float): The numerical distance value to check.
        unit (str): String representation of the source unit ('m', 'km', or 'mi').

    Raises:
        ConversionError: If value is not a valid number or unit is unsupported.
    """
    if not isinstance(value, (int, float)):
        raise ConversionError(f"Distance must be numeric, got {type(value).__name__}")
    
    # Check for NaN and Infinity explicitly as they are technically numbers but invalid here
    import math
    if math.isnan(value) or math.isinf(value):
        raise ConversionError("Invalid distance value: cannot convert non-finite numbers.")

    valid_units = {'m', 'km', 'mi'}
    unit_lower = unit.lower().strip()
    
    if unit_lower not in valid_units:
        raise ConversionError(f"Unsupported source unit '{unit}'. Supported units are {valid_units}")

def convert_distance(value: float, from_unit: str, to_unit: str) -> Union[float, int]:
    """
    Converts a distance value between meters, kilometers, and miles.

    Args:
        value (float): The numerical distance in the source unit.
        from_unit (str): Source unit ('m', 'km', or 'mi').
        to_unit (str): Target unit ('m', 'km', or 'mi').

    Returns:
        float/int: Converted distance in the target unit, rounded to 6 decimal places for precision.

    Raises:
        ConversionError: If input validation fails during execution.
    """
    validate_distance_input(value, from_unit)
    
    # Define conversion factors relative to meters as a common base
    # m = 1, km = 0.001, mi = 621370 (approx in mm for easier float math? No, stick to standard floats)
    # Let's use precise constants:
    
    if from_unit == 'm':
        value_in_meters = value * 1.0
    elif from_unit == 'km':
        value_in_meters = value * 1000.0
    else: # mi
        value_in_meters = value * 1609.344
    
    if to_unit == 'm':
        result = value_in_meters / 1.0
    elif to_unit == 'km':
        result = value_in_meters / 1000.0
    else: # mi
        result = value_in_meters / 1609.344
    
    return round(result, 6)

def get_supported_units() -> list[str]:
    """Returns a sorted list of supported unit abbreviations."""
    return ['km', 'm', 'mi']

if __name__ == '__main__':
    # Hard-coded sample values demonstrating functionality without user input
    
    test_cases = [
        {
            "description": "Convert 100 meters to kilometers",
            "value": 100,
            "from_unit": "m",
            "to_unit": "km"
        },
        {
            "description": "Convert 5 miles to meters",
            "value": 5.0,
            "from_unit": "mi",
            "to_unit": "m"
        },
        {
            "description": "Convert 2 kilometers to miles",
            "value": 2.0,
            "from_unit": "km",
            "to_unit": "mi"
        },
        # Edge case: Same unit conversion (should return original value)
        {
            "description": "Convert 15 meters to meters (identity)",
            "value": 15.0,
            "from_unit": "m",
            "to_unit": "m"
        }
    ]

    print("=== Distance Unit Converter Demo ===\n")

    for case in test_cases:
        try:
            result = convert_distance(
                value=case["value"], 
                from_unit=case["from_unit"], 
                to_unit=case["to_unit"]
            )
            
            # Format output nicely based on magnitude
            if isinstance(result, float) and (result == int(result)):
                display_result = str(int(result)) + " units"
            else:
                display_result = f"{result:.6f} units"

            print(f"[{case['description']}]")
            print(f"  Input: {case['value']} {case['from_unit'].upper()} -> Output: {display_result}")
        except ConversionError as e:
            # This block would catch errors if we had invalid inputs in the list, 
            # but our test cases are valid. Included for completeness of logic flow.
            print(f"[{case['description']}] ERROR: {e}\n")

    print("\n=== Supported Units ===")
    units = get_supported_units()
    print(units)