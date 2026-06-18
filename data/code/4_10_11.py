"""
Distance Unit Converter Module

This module provides functionality to convert distances between miles and kilometers.
It uses a standard conversion factor (1 mile = 1.60934 kilometers) derived from 
the specified requirement context, ensuring production-ready accuracy for general use cases.

The script includes clear input handling via hardcoded sample values within the main block,
ensuring it runs without user interaction or external dependencies.
"""

# Conversion constants defined explicitly as per task requirements
MILES_TO_KILOMETERS_FACTOR = 1.60934
KILOMETERS_TO_MILES_FACTOR = 1 / MILES_TO_KILOMETERS_FACTOR

def convert_distance_miles_to_kilometers(miles: float) -> float:
    """
    Convert a distance from miles to kilometers using the specified conversion factor.
    
    Args:
        miles (float): The distance in miles to be converted.
        
    Returns:
        float: The equivalent distance in kilometers.
    """
    return round(miles * MILES_TO_KILOMETERS_FACTOR, 2)

def convert_distance_kilometers_to_miles(kilometers: float) -> float:
    """
    Convert a distance from kilometers to miles using the specified conversion factor.
    
    Args:
        kilometers (float): The distance in kilometers to be converted.
        
    Returns:
        float: The equivalent distance in miles.
    """
    return round(kilometers * KILOMETERS_TO_MILES_FACTOR, 2)

def format_output(label: str, value_miles: float, value_kilometers: float) -> None:
    """
    Print a formatted result indicating the conversion between units.
    
    Args:
        label (str): A descriptive string for the output context.
        value_miles (float): The original distance in miles.
        value_kilometers (float): The converted distance in kilometers.
        
    Note: This function handles all print statements and ensures no interactive prompts are used.
    """
    print(f"{label}")
    print(f"Miles: {value_miles:.2f} mi")
    print(f"Kilometers: {value_kilometers:.2f} km\n")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external files.
    SAMPLE_MILES = 50.75
    
    # Perform conversion from miles to kilometers using the specified factor
    converted_km = convert_distance_miles_to_kilometers(SAMPLE_MILES)
    
    # Format and display results for both directions of conversion based on sample data
    format_output(
        "Sample Conversion: 50.75 Miles", 
        SAMPLE_MILES, 
        converted_km
    )

    # Additional test case with kilometers to miles using the inverse factor logic
    SAMPLE_KM = 123.456
    
    sample_miles_from_km = convert_distance_kilometers_to_miles(SAMPLE_KM)
    
    format_output(
        "Sample Conversion: 123.456 Kilometers", 
        sample_miles_from_km, 
        SAMPLE_KM
    )

    # Final summary output demonstrating the bidirectional capability with clear labels
    final_summary = """
Conversion Summary using Factor (1 mi ≈ {factor:.4f} km):
{miles_val} miles is equal to {km_val:.2f} kilometers.
"""
    
    print(final_summary.format(
        factor=MILES_TO_KILOMETERS_FACTOR, 
        miles_val=SAMPLE_MILES, 
        km_val=converted_km
    ))