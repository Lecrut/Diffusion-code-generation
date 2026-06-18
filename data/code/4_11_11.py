class DistanceConverter:
    """A class to convert distances between miles and kilometers."""

    def __init__(self):
        self._conversion_factor = 1.60934  # Miles per kilometer (inverse of km/mi) for mi->km conversion logic below

    def _validate_input(self, value):
        """Validate that the input is a numeric type and raise ValueError if not."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        
        # Handle infinity or NaN cases for robustness
        import math
        if math.isnan(value) or math.isinf(value):
            raise ValueError("Input cannot contain infinite values or NaN.")

    def miles_to_kilometers(self, value):
        """Convert distance from miles to kilometers.
        
        Args:
            value (int|float): Distance in miles.
            
        Returns:
            float: Equivalent distance in kilometers.
            
        Raises:
            TypeError: If input is not a number.
            ValueError: If input contains infinity or NaN.
        """
        self._validate_input(value)
        return value * 1.60934

    def kilometers_to_miles(self, value):
        """Convert distance from kilometers to miles.
        
        Args:
            value (int|float): Distance in kilometers.
            
        Returns:
            float: Equivalent distance in miles.
            
        Raises:
            TypeError: If input is not a number.
            ValueError: If input contains infinity or NaN.
        """
        self._validate_input(value)
        return value / 1.60934

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    
    converter = DistanceConverter()

    # Sample test cases
    try:
        # Test miles to kilometers
        result_mi_km = converter.miles_to_kilometers(10)
        print(f"{result_mi_km:.2f} km")  # Expected approx 16.0934
        
        # Test negative values (should work mathematically, though physically distance is positive)
        result_neg = converter.kilometers_to_miles(-5)
        print(f"Negative conversion: {result_neg:.2f} miles")

        # Test non-numeric input validation
        try:
            converter.miles_to_kilometers("ten")
        except TypeError as e:
            print(f"Caught expected error for string input: {e}")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")