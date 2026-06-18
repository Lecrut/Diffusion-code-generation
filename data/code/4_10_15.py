"""
Module: distance_unit_converter.py

This script demonstrates how to correctly adjust distance units between miles 
and kilometers using a specified conversion factor. It includes clear input handling,
output formatting, and runs with hard-coded sample values without requiring any user interaction or external dependencies.

Conversion Factors used in this module (standard approximations):
- 1 mile = 1.609344 kilometers
- 1 kilometer = 0.621371 miles
"""

def convert_miles_to_kilometers(miles: float, factor: float) -> float:
    """
    Convert distance from miles to kilometers using a specified conversion factor.

    Args:
        miles (float): The distance in miles.
        factor (float): The conversion factor where 1 mile = X km (default is standard).

    Returns:
        float: The converted distance in kilometers, rounded to two decimal places.
    """
    return round(miles * factor, 2)

def convert_kilometers_to_miles(km: float, inverse_factor: float) -> float:
    """
    Convert distance from kilometers to miles using a specified conversion factor.

    Args:
        km (float): The distance in kilometers.
        inverse_factor (float): The conversion factor where 1 km = X miles (default is standard).

    Returns:
        float: The converted distance in miles, rounded to two decimal places.
    """
    return round(km * inverse_factor, 2)

def format_output(label: str, original_value: float, unit_original: str, 
                 result_value: float, target_unit: str) -> None:
    """
    Print a formatted output block showing the conversion details.

    Args:
        label (str): A descriptive header for this conversion step.
        original_value (float): The input value before conversion.
        unit_original (str): The source unit of measurement.
        result_value (float): The calculated converted value.
        target_unit (str): The destination unit of measurement.
    """
    print(f"{label}")
    print(f"  Input: {original_value} {unit_original}")
    print(f"  Output: {result_value} {target_unit}")

if __name__ == '__main__':
    # Standard conversion factors (ISO standard)
    MILES_TO_KM_FACTOR = 1.609344
    KM_TO_MILES_INVERSE_FACTOR = 1 / MILES_TO_KM_FACTOR

    print("=" * 50)
    print("Distance Unit Converter Demo")
    print("=" * 50)

    # Hard-coded sample values as per requirements (no input(), sys.stdin, or args)
    SAMPLE_MILES = 3.74821569
    SAMPLE_KM = 6.023
    
    print("\n--- Conversion from Miles to Kilometers ---")
    
    result_km = convert_miles_to_kilometers(SAMPLE_MILES, MILES_TO_KM_FACTOR)
    format_output(
        label=f"Converting {SAMPLE_MILES} miles",
        original_value=SAMPLE_MILES,
        unit_original="miles",
        result_value=result_km,
        target_unit="kilometers"
    )

    print("\n--- Conversion from Kilometers to Miles ---")
    
    result_miles = convert_kilometers_to_miles(SAMPLE_KM, KM_TO_MILES_INVERSE_FACTOR)
    format_output(
        label=f"Converting {SAMPLE_KM} kilometers",
        original_value=SAMPLE_KM,
        unit_original="kilometers",
        result_value=result_miles,
        target_unit="miles"
    )

    print("=" * 50)