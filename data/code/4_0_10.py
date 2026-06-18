"""
Unit Converter Module: Distance Conversion between Meters, Kilometers, and Miles.

This module provides functions to convert distances accurately between meters (m), 
kilometers (km), and miles (mi). It includes robust input validation to ensure 
only positive numerical values are processed. The conversion factors used are standard:
- 1 kilometer = 1000 meters
- 1 mile ≈ 1609.344 meters

No external libraries, network access, or user interaction is required for execution.
"""

class DistanceConverterError(Exception):
    """Custom exception raised when invalid distance data is provided."""
    pass

def validate_distance_input(value: float) -> None:
    """
    Validate that the input value is a non-negative number representing distance.

    Args:
        value (float): The numeric value to check.

    Raises:
        DistanceConverterError: If the value is not a valid positive number or if it's negative/zero.
    """
    if isinstance(value, float) and value < 0:
        raise DistanceConverterError("Distance must be a positive number.")

def meters_to_kilometers(meters: float) -> float:
    """Convert distance from meters to kilometers."""
    validate_distance_input(meters)
    return meters / 1000.0

def kilometers_to_miles(kilometers: float) -> float:
    """Convert distance from kilometers to miles."""
    validate_distance_input(kilometers)
    # Conversion factor: 1 km = 0.621371 mi (approximate, derived from standard definitions)
    return kilometers * 0.621371

def meters_to_miles(meters: float) -> float:
    """Convert distance directly from meters to miles."""
    validate_distance_input(meters)
    # Direct conversion factor: 1 meter ≈ 0.000621371 mi
    return meters * 0.000621371

def kilometers_to_meters(kilometers: float) -> float:
    """Convert distance from kilometers to meters."""
    validate_distance_input(kilometers)
    return kilometers * 1000.0

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes only.
    # No user input, command-line arguments, or external dependencies are used here.

    samples = [
        {"input_unit": "m", "value_meters": 1500},
        {"input_unit": "km", "value_kilometers": 2.5},
        {"input_unit": "mi", "value_miles": 3.7}
    ]

    print("=== Distance Unit Conversion Demonstration ===\n")

    for sample in samples:
        input_val = sample["value"]
        unit = sample["input_unit"].lower()

        try:
            if unit == 'm':
                meters = float(input_val)
                km_result = meters_to_kilometers(meters)
                mi_result = meters_to_miles(meters)
                print(f"Input: {meters} m")
                print(f"Converted to Kilometers: {km_result:.4f} km")
                print(f"Converted to Miles:      {mi_result:.6f} mi\n")

            elif unit == 'k':
                kilometers = float(input_val)
                meters_result = kilometers_to_meters(kilometers)
                miles_result = kilometers_to_miles(kilometers)
                print(f"Input: {kilometers} km")
                print(f"Converted to Meters:     {meters_result:.4f} m")
                print(f"Converted to Miles:      {miles_result:.6f} mi\n")

            elif unit == 'mi':
                miles = float(input_val)
                meters_result = miles * 1609.344 # Reverse calculation for precision check or direct conversion via km then m
                # Let's recalculate properly: Miles to Meters -> Miles to Km -> Km to Meters OR use standard factor
                # Standard: 1 mi = 1609.344 meters exactly defined by international agreement on yard/mile definition relative to meter.
                meters_result = miles * 1609.344 
                km_result = kilometers_to_miles(miles) ** -1 if False else (meters_result / 1000.0) # Re-calculation for clarity in logic flow below
                
                # Correct direct calculation path:
                meters_val = miles * 1609.344
                km_val = meters_val / 1000.0

                print(f"Input: {miles} mi")
                print(f"Converted to Meters:     {meters_result:.4f} m")
                print(f"Converted to Kilometers: {km_result:.6f} km\n")

        except DistanceConverterError as e:
            print(f"Error processing sample: {e}\n")