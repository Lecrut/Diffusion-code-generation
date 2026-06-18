"""
Meters to Feet Converter Module

This module provides functionality to convert lengths from meters to feet.
The conversion uses the standard factor: 1 meter = 3.28084 feet.
"""

def convert_meters_to_feet(meters: float) -> float:
    """
    Converts a length given in meters to its equivalent in feet.

    Args:
        meters (float): The length value in meters. Must be non-negative for physical 
                       lengths, though the function will process negative values mathematically.

    Returns:
        float: The converted length in feet.

    Raises:
        TypeError: If the input is not a numeric type.
    
    Examples:
        >>> convert_meters_to_feet(1)
        3.28084
    
        >>> convert_meters_to_feet(5.5)
        18.04462
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be a number.")

    conversion_factor = 3.28084
    
    return meters * conversion_factor

def main():
    """
    Main execution block with hard-coded sample values for demonstration.
    
    This function demonstrates the usage of convert_meters_to_feet by 
    processing predefined meter values and printing the results to stdout.
    It does not require any user input during normal operation.
    """
    # Sample data: list of meters to convert
    sample_lengths = [1, 2.5, 10, -3]

    print("Meters to Feet Conversion Results")
    print("-" * 40)
    
    for length in sample_lengths:
        try:
            feet_value = convert_meters_to_feet(length)
            # Format output with appropriate precision based on input magnitude
            if isinstance(length, int):
                formatted_output = f"{length} m = {feet_value:.2f} ft"
            else:
                formatted_output = f"{length} m = {feet_value:.4f} ft"
            
            print(formatted_output)
        except TypeError as e:
            # Handle cases where input might not be a number (though sample data ensures this won't happen here)
            print(f"Error converting {length}: {e}")

if __name__ == '__main__':
    main()