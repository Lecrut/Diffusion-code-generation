"""
Unit Conversion Module: Distance Converter between Meters, Kilometers, and Miles.

This module provides functions to convert distance values accurately between 
meters (m), kilometers (km), and miles (mi). It includes robust input validation 
to ensure only positive numeric values are processed for physical distances.

Conversion Factors:
- 1 kilometer = 1000 meters
- 1 mile ≈ 1609.344 meters

The module is designed to be production-ready with clear error handling and no external dependencies.
"""

class DistanceConverterError(Exception):
    """Custom exception for invalid distance conversion inputs."""
    pass

def validate_distance(value: float) -> None:
    """
    Validate that the input value is a positive number representing a valid distance.

    Args:
        value (float): The distance value to validate.

    Raises:
        DistanceConverterError: If the value is not numeric, negative, or zero.
    """
    if not isinstance(value, (int, float)):
        raise DistanceConverterError(f"Invalid input type: expected number, got {type(value).__name__}")
    
    if value <= 0:
        raise DistanceConverterError("Distance must be a positive number greater than zero.")

def meters_to_kilometers(meters: float) -> float:
    """Convert distance from meters to kilometers.

    Args:
        meters (float): The distance in meters.

    Returns:
        float: The equivalent distance in kilometers.
    """
    validate_distance(meters)
    return meters / 1000

def kilometers_to_meters(kilometers: float) -> float:
    """Convert distance from kilometers to meters.

    Args:
        kilometers (float): The distance in kilometers.

    Returns:
        float: The equivalent distance in meters.
    """
    validate_distance(kilometers)
    return kilometers * 1000

def miles_to_meters(miles: float) -> float:
    """Convert distance from miles to meters.

    Args:
        miles (float): The distance in miles.

    Returns:
        float: The equivalent distance in meters.
    """
    validate_distance(miles)
    return miles * 1609.344

def meters_to_miles(meters: float) -> float:
    """Convert distance from meters to miles.

    Args:
        meters (float): The distance in meters.

    Returns:
        float: The equivalent distance in miles.
    """
    validate_distance(meters)
    return meters / 1609.344

def kilometers_to_miles(kilometers: float) -> float:
    """Convert distance from kilometers to miles.

    Args:
        kilometers (float): The distance in kilometers.

    Returns:
        float: The equivalent distance in miles.
    """
    validate_distance(kilometers)
    return kilometers / 1609.344 * 1000

def convert_miles_to_kilometers(miles: float) -> float:
    """Convert distance from miles to kilometers.

    Args:
        miles (float): The distance in miles.

    Returns:
        float: The equivalent distance in kilometers.
    """
    validate_distance(miles)
    return miles * 1609.344 / 1000

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or CLI arguments
    
    samples = [
        {"input_unit": "meters", "value": 500},      # Convert to km and mi
        {"input_unit": "kilometers", "value": 2.5},   # Convert to m, km (idempotent check), mi
        {"input_unit": "miles", "value": 3}           # Convert to m, km
    ]

    print("=== Distance Unit Conversion Demo ===\n")

    for sample in samples:
        unit = sample["input_unit"]
        value = sample["value"]
        
        try:
            if unit == "meters":
                meters = float(value)
                kilometers = meters_to_kilometers(meters)
                miles = meters_to_miles(meters)
                
                print(f"Input: {value} Meters")
                print(f"  -> Kilometers: {kilometers:.4f}")
                print(f"  -> Miles:      {miles:.6f}\n")

            elif unit == "kilometers":
                kilometers = float(value)
                meters = kilometers_to_meters(kilometers)
                miles = kilometers_to_miles(kilometers)
                
                # Also test reverse km->km for idempotency check logic implicitly via conversion chain if needed, 
                # but here we just show conversions to other units.
                print(f"Input: {value} Kilometers")
                print(f"  -> Meters:      {meters:.4f}")
                print(f"  -> Miles:       {miles:.6f}\n")

            elif unit == "miles":
                miles = float(value)
                meters = miles_to_meters(miles)
                kilometers = convert_miles_to_kilometers(miles)
                
                print(f"Input: {value} Miles")
                print(f"  -> Meters:      {meters:.4f}")
                print(f"  -> Kilometers:  {kilometers:.6f}\n")

        except DistanceConverterError as e:
            print(f"Conversion Error for sample '{unit}' ({value}): {e}\n")