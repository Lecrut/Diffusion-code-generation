"""
Module: distance_converter_miles_km

This script demonstrates how to correctly adjust distance units between miles 
and kilometers using a specified conversion factor. It includes clear input handling 
and output formatting, operating entirely with hard-coded sample values in the main block.

Conversion logic uses standard factors for accuracy without external dependencies or interactive prompts.
"""

def convert_miles_to_kilometers(miles: float) -> dict[str, str]:
    """
    Convert a distance given in miles to kilometers using a precise conversion factor.
    
    Args:
        miles (float): The distance in miles.
        
    Returns:
        dict[str, str]: A dictionary containing the original value and converted result 
                        formatted as strings with appropriate units.
    """
    # Standard conversion factor: 1 mile = 1.60934 kilometers
    CONVERSION_FACTOR = 1.60934
    
    if miles < 0:
        raise ValueError("Distance cannot be negative.")
    
    kilometers = miles * CONVERSION_FACTOR
    
    return {
        "input_miles": f"{miles:.2f} mi",
        "conversion_factor_str": str(CONVERSION_FACTOR),
        "output_kilometers": f"{kilometers:.4f} km"
    }

def convert_kilometers_to_miles(kilometers: float) -> dict[str, str]:
    """
    Convert a distance given in kilometers to miles using the inverse conversion factor.
    
    Args:
        kilometers (float): The distance in kilometers.
        
    Returns:
        dict[str, str]: A dictionary containing the original value and converted result 
                        formatted as strings with appropriate units.
    """
    # Inverse conversion factor derived from standard definition
    CONVERSION_FACTOR_INV = 1 / 1.60934
    
    if kilometers < 0:
        raise ValueError("Distance cannot be negative.")
    
    miles = kilometers * CONVERSION_FACTOR_INV
    
    return {
        "input_kilometers": f"{kilometers:.2f} km",
        "conversion_factor_str": str(CONVERSION_FACTOR_INV),
        "output_miles": f"{miles:.4f} mi"
    }

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No user input, command-line arguments, or network access is required.
    
    SAMPLE_MILES = 100.0
    
    print("=" * 50)
    print("Distance Unit Converter: Miles to Kilometers")
    print("=" * 50)
    
    result_miles_to_km = convert_miles_to_kilometers(SAMPLE_MILES)
    
    # Output results formatted clearly for the user
    print(f"Input Distance (Miles): {result_miles_to_km['input_miles']}")
    print(f"Conversion Factor Used: 1 mile ≈ {result_miles_to_km['conversion_factor_str']} km")
    print(f"Converted Distance (Kilometers): {result_miles_to_km['output_kilometers']}\n")
    
    # Demonstrate the reverse conversion using a sample from the first result to show bidirectional logic
    SAMPLE_KM = 30.0
    
    print("=" * 50)
    print("Distance Unit Converter: Kilometers to Miles (Reverse)")
    print("=" * 50)
    
    # Using a specific value that results in an integer mile count for clarity demonstration if desired, 
    # or simply another sample as per task requirements. Here we use the calculated km from above rounded slightly 
    # plus a small offset just to show it works with different inputs, but strictly following "hard-coded" requirement:
    
    SAMPLE_KM = 50.0
    
    result_km_to_miles = convert_kilometers_to_miles(SAMPLE_KM)
    
    print(f"Input Distance (Kilometers): {result_km_to_miles['input_kilometers']}")
    print(f"Inverse Conversion Factor Used: ~{result_km_to_miles['conversion_factor_str']:.6f} mi/km")
    print(f"Converted Distance (Miles): {result_km_to_miles['output_miles']}\n")
    
    # Final summary block to ensure the script completes successfully without errors or prompts.
    print("Conversion process completed successfully.")