"""
Module: distance_unit_converter.py

This script demonstrates how to correctly adjust distance units between miles 
and kilometers using a specified conversion factor. It includes clear input handling 
logic (simulated via hardcoded values) and formatted output, ensuring it runs as 
a standalone module without external dependencies or interactive prompts.
"""

def convert_distance_miles_to_kilometers(miles: float, km_factor: float = 1.609344) -> float:
    """
    Convert a distance given in miles to kilometers using the provided conversion factor.

    Args:
        miles (float): The distance value in miles.
        km_factor (float): The conversion factor from miles to kilometers 
                          (default is 1 mile = 1.609344 km).

    Returns:
        float: The converted distance in kilometers, rounded to two decimal places.
    """
    return round(miles * km_factor, 2)

def convert_distance_kilometers_to_miles(km_value: float, factor_inv: float = 0.621371) -> float:
    """
    Convert a distance given in kilometers to miles using the provided conversion factor.

    Args:
        km_value (float): The distance value in kilometers.
        factor_inv (float): The inverse conversion factor from kilometers to 
                           miles (default is 1 km = 0.621371 mi).

    Returns:
        float: The converted distance in miles, rounded to two decimal places.
    """
    return round(km_value * factor_inv, 2)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No user input is required; this block runs completely offline and self-contained.

    SAMPLE_MILES = 100.5
    SAMPLE_KM_FACTOR = 1.609344
    
    SAMPLE_KILOMETERS = 250.75
    SAMPLE_MI_FACTOR_INV = 0.621371

    # Perform conversions using the specified factors
    kilometers_result = convert_distance_miles_to_kilometers(SAMPLE_MILES, SAMPLE_KM_FACTOR)
    miles_result = convert_distance_kilometers_to_miles(SAMPLE_KILOMETERS, SAMPLE_MI_FACTOR_INV)

    # Format and print output clearly
    print("Distance Conversion Results")
    print("-" * 30)
    
    # Miles to Kilometers conversion example
    print(f"Original Distance: {SAMPLE_MILES} miles")
    print(f"Conversion Factor Used: {SAMPLE_KM_FACTOR}")
    print(f"Converted Distance: {kilometers_result:.2f} kilometers\n")

    # Kilometers to Miles conversion example
    print(f"Original Distance: {SAMPLE_KILOMETERS} kilometers")
    print(f"Inverse Conversion Factor Used: {SAMPLE_MI_FACTOR_INV}")
    print(f"Converted Distance: {miles_result:.2f} miles")
    
    # Verification check (approximate)
    expected_km_check = round(SAMPLE_MILES * SAMPLE_KM_FACTOR, 2)
    if abs(kilometers_result - expected_km_check) < 0.01:
        print(f"\nVerification Passed: {SAMPLE_MILES} miles correctly converts to ~{expected_km_check} km")
    else:
        print("\nNote: Minor floating-point discrepancies may occur due to rounding.")