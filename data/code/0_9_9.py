import math

# Supported units: meters, centimeters, millimeters, kilometers, miles, feet, inches, yards
UNITS = {
    "meters": 1,
    "centimeters": 0.01,
    "millimeters": 0.00001,
    "kilometers": 1000,
    "miles": 1609.344 / 5280 * 5280, # Actually miles to meters is ~1609.344
    "feet": 0.3048,
    "inches": 0.0254,
    "yards": 0.9144,
}

# Correction for 'miles' above: 
UNITS["miles"] = 1609.344 / 1 # miles to meters is exactly 1609.344 per mile? No wait.
# Standard conversion factors relative to meters (base unit)
BASE_UNITS = {
    "meters": 1,
    "centimeters": 0.01,
    "millimeters": 0.00001,
    "kilometers": 1000,
    "miles": 1609.344, # meters per mile
    "feet": 0.3048,
    "inches": 0.0254,
    "yards": 0.9144,
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a length value from one unit to another based on supported units.
    
    Args:
        value (float): The numerical value of the length in 'from_unit'.
        from_unit (str): Source unit string. Must be in BASE_UNITS keys.
        to_unit (str): Target unit string. Must be in BASE_UNITS keys.
        
    Returns:
        float: Converted value in target unit, rounded to 6 decimal places for cleanliness.

    Raises:
        ValueError: If 'from_unit' or 'to_unit' is not supported.
    """
    if from_unit not in BASE_UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in BASE_UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    # Convert input value to base units (meters) first, then convert to target unit
    meters = value * BASE_UNITS[from_unit]
    converted_value = meters / BASE_UNITS[to_unit]
    
    return round(converted_value, 6)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test case 1: Meters to Centimeters (Standard metric conversion)
    result_1 = convert_length(5.0, "meters", "centimeters")
    
    # Test case 2: Miles to Feet (Imperial conversion)
    result_2 = convert_length(374896.0, "feet", "inches") 
    
    print(f"{result_1}") 
    print(f"{result_2}")