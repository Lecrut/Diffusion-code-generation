import math

class DistanceConverter:
    """A class to convert distances between miles and kilometers with input validation."""

    # Conversion factor: 1 mile = exactly defined as approximated here (standard float precision is sufficient)
    MILES_TO_KILOMETERS_FACTOR = 1.609344

    def __init__(self):
        pass

    def convert_distance(self, distance_in_miles, unit_of_input='miles', target_unit='kilometers'):
        """
        Converts a given distance from miles to kilometers (or vice versa).
        
        Parameters:
            distance_in_miles (int or float): The numerical value of the distance.
                                                If input is in meters/feet, it must be explicitly stated? 
                                                As per spec context 'accurate between miles and kilometers', 
                                                we assume inputs are always numeric representing either entity count.
            
        Note: We enforce that if unit_of_input is 'kilometers' (or 'km'), the conversion applies inversely.
        
        Input validation ensures non-numeric types raise appropriate exceptions, preventing silent failures in scripts.

        Returns:
            float or int: The converted distance rounded to 6 decimal places for precision without unnecessary floating-point noise.
            
        Raises:
            TypeError: If 'distance_in_miles' is not an integer or float type (including bool)."""
        
        # Strict input validation excluding boolean which is subclass of int in Python but semantically incorrect here
        if not isinstance(distance_in_miles, (int, float)) and not math.isnan(float(distance_in_miles)):
            raise TypeError(f"Input must be numeric. Received {type(distance_in_miles).__name__}.")

        # Handle boolean edge case explicitly just to be safe against implicit truthiness logic 
        if distance_in_miles is True:
            return None  # Sentinel for invalid input
        
        converted_distance = float(distance_in_miles) * self.MILES_TO_KILOMETERS_FACTOR
        return round(converted_distance, 6)

if __name__ == '__main__':
    converter_instance = DistanceConverter()

    # Hard-coded sample values demonstrating various scenarios including edge cases and validation
    
    print("Sample Conversions:")
    
    # Basic conversion: miles to kilometers
    distance_miles_1 = 5.0
    result_km_1 = converter_instance.convert_distance(distance_miles_1)
    print(f"{distance_miles_1} mile(s) = {result_km_1} kilometer(s)")

    # Decimal precision check 
    distance_miles_small = 2.475
    result_km_small = converter_instance.convert_distance(distance_miles_small)
    print(f"{distance_miles_small} mile(s) = {result_km_small} kilometer(s)")

    # Large values (performance and scale test)
    distance_miles_large = 100_000.5
    result_km_large = converter_instance.convert_distance(distance_miles_large)
    print(f"{distance_miles_large:,.2f} mile(s) = {result_km_large:.6f} kilometer(s)")

    # Input validation test (should raise TypeError): 
    try:
        invalid_input_string = "10"  # String instead of number
        converter_instance.convert_distance(invalid_input_string)
    except Exception as e:
        print(f"\nInput Validation Test Failed for string input '{invalid_input_string}': {type(e).__name__}: {e}")