import math

# Conversion constants defined as class attributes to avoid global namespace pollution
class UnitConverter:
    MILES_TO_KM_FACTOR = 1.609344
    KM_TO_MILES_FACTOR = 0.621371
    
    def __init__(self, factor):
        """Initialize the converter with a specific conversion factor."""
        self.factor = factor
        
    def convert_distance(self, value_in_miles) -> float:
        """Convert distance from miles to kilometers using the specified factor."""
        return round(value_in_miles * self.factor, 2)

def format_output(distance_km):
    """Format the output string for readability."""
    if isinstance(distance_km, (int, float)):
        formatted = f"{distance_km:.1f}"
        # Ensure it doesn't end in .0 unless necessary by checking integer-ness before rounding logic above
        return str(int(formatted)) + " km" if "." not in formatted else formatted + " km"
    return distance_km

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    
    # Sample 1: Standard conversion using the standard factor
    miles_sample_1 = 5.0
    
    # Create converter instance with default standard factor
    std_converter = UnitConverter(UnitConverter.MILES_TO_KM_FACTOR)
    
    km_result_1 = std_converter.convert_distance(miles_sample_1)
    formatted_output_1 = format_output(km_result_1)
    
    print(f"Sample 1: {miles_sample_1} miles is equal to {formatted_output_1}")

    # Sample 2: Using a custom conversion factor for demonstration (e.g., simplified approximation)
    custom_factor = 1.6
    
    km_converter_custom = UnitConverter(custom_factor)
    
    miles_sample_2 = 30.5
    km_result_2 = km_converter_custom.convert_distance(miles_sample_2)
    formatted_output_2 = format_output(km_result_2)
    
    print(f"Sample 2: {miles_sample_2} miles is equal to {formatted_output_2}")

    # Sample 3: Edge case with very small distance
    miles_sample_3 = 0.1
    
    km_converter_small = UnitConverter(UnitConverter.MILES_TO_KM_FACTOR)
    
    km_result_3 = km_converter_small.convert_distance(miles_sample_3)
    formatted_output_3 = format_output(km_result_3)
    
    print(f"Sample 3: {miles_sample_3} miles is equal to {formatted_output_3}")

    # Verification of reverse conversion logic consistency (optional internal check, not printed)
    assert abs(UnitConverter.MILES_TO_KM_FACTOR - UnitConverter.KM_TO_MILES_FACTOR**-1) < 0.0001
    
    print("All conversions completed successfully.")