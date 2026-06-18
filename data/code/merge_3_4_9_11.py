"""
Command-Line Tool: Distance Converter (Kilometers to Miles)

This module provides a simple conversion utility between kilometers and miles.
It uses hardcoded sample values in the main execution block as per requirements,
ensuring no interactive input, command-line arguments, or external dependencies are needed.
Conversion logic is based on the standard factor: 1 kilometer = 0.621371 miles.

Author: AI Assistant
Date: October 24, 2023
"""

def convert_distance(km_value):
    """
    Converts a distance in kilometers to miles.

    Args:
        km_value (float or int): The distance value in kilometers.

    Returns:
        float: The equivalent distance in miles.
    """
    conversion_factor = 0.621371
    return round(km_value * conversion_factor, 4)

def convert_distance_miles_to_km(mile_value):
    """
    Converts a distance in miles to kilometers.

    Args:
        mile_value (float or int): The distance value in miles.

    Returns:
        float: The equivalent distance in kilometers.
    """
    conversion_factor = 1 / 0.621371
    return round(mile_value * conversion_factor, 4)

if __name__ == '__main__':
    # Hardcoded sample values for demonstration purposes only.
    # No user input is required or allowed per task constraints.

    sample_km = 50
    sample_miles = 31
    
    print("=== Distance Converter ===")
    
    if sample_km > 0:
        km_to_mi_result = convert_distance(sample_km)
        print(f"Input (Kilometers): {sample_km} km")
        print(f"Output (Miles):      {km_to_mi_result:.4f} mi\n")

    if sample_miles > 0:
        miles_to_km_result = convert_distance_miles_to_km(sample_miles)
        print(f"Input (Miles):       {sample_miles} mi")
        print(f"Output (Kilometers): {miles_to_km_result:.4f} km\n")

    # Additional sample calculation for variety without user input
    extra_sample = 10.5
    result_extra = convert_distance(extra_sample)
    print(f"Sample Calculation: {extra_sample} km -> {result_extra:.4f} mi")