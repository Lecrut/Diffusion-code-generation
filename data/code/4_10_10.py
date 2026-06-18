"""
Distance Unit Converter Module

This module provides functionality to convert distances between miles and kilometers
using a specified conversion factor. It includes logic to handle both directions of
conversion (miles -> km, km -> mi) with clear input validation and output formatting.

Conversion Factors:
- 1 mile = 1.60934 kilometers (standard international value used for precision)
"""

class DistanceConverter:
    """A class to convert distances between miles and kilometers."""
    
    def __init__(self, conversion_factor: float):
        """
        Initialize the converter with a specific conversion factor.

        Args:
            conversion_factor (float): The multiplier to use for converting 
                                      distance in one unit to another. 
                                      For standard usage, 1 mile = 1.60934 km.
        Raises:
            ValueError: If the conversion factor is not a positive number.
        """
        if conversion_factor <= 0:
            raise ValueError("Conversion factor must be a positive number.")
        
        self.conversion_factor = conversion_factor
    
    def convert_miles_to_kilometers(self, distance_in_miles: float) -> dict:
        """
        Convert a distance from miles to kilometers.

        Args:
            distance_in_miles (float): The distance in miles to convert.

        Returns:
            dict: A dictionary containing the original value and converted result.
                  Example: {'original_unit': 'miles', 'value': 5, 
                           'converted_value': 8.0467}
        """
        if not isinstance(distance_in_miles, (int, float)):
            raise TypeError("Distance input must be a number.")

        converted_kilometers = distance_in_miles * self.conversion_factor
        
        return {
            "original_unit": "miles",
            "input_value": round(distance_in_miles, 4),
            "converted_unit": "kilometers",
            "output_value": round(converted_kilometers, 2)
        }

    def convert_kilometers_to_miles(self, distance_in_km: float) -> dict:
        """
        Convert a distance from kilometers to miles.

        Args:
            distance_in_km (float): The distance in kilometers to convert.

        Returns:
            dict: A dictionary containing the original value and converted result.
                  Example: {'original_unit': 'kilometers', 'value': 8, 
                           'converted_value': 4.97}
        """
        if not isinstance(distance_in_km, (int, float)):
            raise TypeError("Distance input must be a number.")

        # Recalculate the factor for km to miles based on the provided forward factor
        # If 1 mile = F km, then 1 km = 1/F miles
        conversion_factor_reverse = round(1 / self.conversion_factor)

        converted_miles = distance_in_km * conversion_factor_reverse
        
        return {
            "original_unit": "kilometers",
            "input_value": round(distance_in_km, 4),
            "converted_unit": "miles",
            "output_value": round(converted_miles, 2)
        }

def main():
    """
    Main execution block.

    Demonstrates the DistanceConverter class with hard-coded sample values 
    to show correct distance unit adjustment between miles and kilometers.
    
    Since no user input is required or allowed per task specifications:
    - Uses predefined test cases within this function.
    - Prints formatted output for each conversion scenario.
    """

    # Initialize converter using the standard factor where 1 mile = 1.60934 km
    converter = DistanceConverter(conversion_factor=1.60934)

    print("=" * 50)
    print("Distance Unit Converter Demo")
    print(f"Conversion Factor Used: {converter.conversion_factor} (km per mile)")
    print("-" * 50)

    # Sample Case 1: Convert miles to kilometers
    sample_miles = 2.3456789
    
    result_mi_to_km = converter.convert_miles_to_kilometers(sample_miles)
    
    print(f"\nSample Input (Miles): {result_mi_to_km['input_value']}")
    print("Original Unit:       ", result_mi_to_km["original_unit"])
    print("Converted Value:      ", f"{result_mi_to_km['output_value']:.2f}")
    print("New Unit:             ", result_mi_to_km["converted_unit"])

    # Sample Case 2: Convert kilometers to miles (inverse operation)
    sample_kilometers = 10.5
    
    result_km_to_mi = converter.convert_kilometers_to_miles(sample_kilometers)
    
    print(f"\nSample Input (Kilometers): {result_km_to_mi['input_value']}")
    print("Original Unit:       ", result_km_to_mi["original_unit"])
    print("Converted Value:      ", f"{result_km_to_mi['output_value']:.2f}")
    print("New Unit:             ", result_km_to_mi["converted_unit"])

    # Sample Case 3: Edge case - Very small value
    sample_small = 0.001
    
    result_small = converter.convert_miles_to_kilometers(sample_small)
    
    print(f"\nSample Input (Miles): {result_small['input_value']}")
    print("Original Unit:       ", result_small["original_unit"])
    print("Converted Value:      ", f"{result_small['output_value']:.4f}")
    print("New Unit:             ", result_small["converted_unit"])

    # Sample Case 4: Edge case - Large value
    sample_large = 100
    
    result_large = converter.convert_miles_to_kilometers(sample_large)
    
    print(f"\nSample Input (Miles): {result_large['input_value']}")
    print("Original Unit:       ", result_large["original_unit"])
    print("Converted Value:      ", f"{result_large['output_value']:.2f}")
    print("New Unit:             ", result_large["converted_unit"])

    # Demonstrate error handling for invalid input type (commented out to avoid runtime errors in demo)
    # Uncommenting the line below would trigger an exception during execution if run directly.
    # converter.convert_miles_to_kilometers("invalid_string") 

    print("-" * 50)
    print("Conversion process completed successfully.")

if __name__ == '__main__':
    main()