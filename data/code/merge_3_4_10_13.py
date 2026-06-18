"""
Distance Unit Converter Module

This module provides a function to convert distances between miles and kilometers
using a specified conversion factor. It includes input handling, validation, 
and formatted output suitable for production use without requiring user interaction.
"""

def convert_distance(distance_miles: float, conversion_factor: float) -> dict[str, str]:
    """
    Converts a distance from miles to kilometers using the provided conversion factor.

    Args:
        distance_miles (float): The distance value in miles. Must be non-negative.
        conversion_factor (float): The multiplier to convert miles to kilometers 
                                   (default is 1.60934, but can be overridden).

    Returns:
        dict[str, str]: A dictionary containing the original input and converted output strings.

    Raises:
        ValueError: If distance_miles or conversion_factor are negative.
    
    Example usage:
        >>> result = convert_distance(10.5)
        print(result['input'])  # "Input Distance (miles): 10.5"
        print(result['output'])# "Converted Distance (kilometers): 16.89807"
    """
    
    if distance_miles < 0:
        raise ValueError("Distance in miles cannot be negative.")
    if conversion_factor <= 0:
        raise ValueError("Conversion factor must be positive.")

    # Perform the calculation using standard precision for display purposes
    converted_km = round(distance_miles * conversion_factor, 4)

    return {
        "input": f"Input Distance (miles): {distance_miles}",
        "output": f"Converted Distance (kilometers): {converted_km}"
    }

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies.
    
    # Sample 1: Standard conversion using default factor logic if not overridden, 
    # but here we explicitly pass the standard factor to demonstrate control over precision.
    miles_sample_1 = 50.762934
    km_factor_standard = 1.60934
    
    result_1 = convert_distance(miles_sample_1, km_factor_standard)

    # Sample 2: Using a custom conversion factor for demonstration of flexibility
    miles_sample_2 = 10
    km_factor_custom = 1.5 

    result_2 = convert_distance(miles_sample_2, km_factor_custom)

    print(result_1['input'])
    print()
    print(result_1['output'])
    
    print("\n--- Sample with Custom Factor ---")
    print(result_2['input'])
    print()
    print(result_2['output'])