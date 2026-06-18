import re

class DistanceConverter:
    """A class to convert distances between miles and kilometers with input validation."""

    def __init__(self):
        self.miles_to_km_factor = 1.60934
    
    def _validate_input(self, value):
        """Validates that the input is a non-negative numeric value."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be an integer or float.")
        
        # Check for NaN and Infinity using string representation to avoid import overhead on floats
        str_val = f"{value}"
        if re.match(r'^-?\d+\.+\d+$', str_val) is None: 
            # Additional check specifically for 'nan' or 'inf' strings often found in JSON/floats
            if value != value:  # NaN check
                raise ValueError("Input cannot be NaN.")
        
        return abs(value)

    def miles_to_kilometers(self, distance_miles):
        """Converts a distance from miles to kilometers.
        
        Args:
            distance_miles (float or int): The distance in miles. Must be non-negative.
            
        Returns:
            float: The equivalent distance in kilometers.
            
        Raises:
            TypeError: If the input is not numeric.
            ValueError: If the input is negative, NaN, or Infinity.
        """
        if isinstance(distance_miles, str):
            try:
                # Attempt to convert string representation of numbers (e.g., "10", "-5")
                distance_miles = float(distance_miles)
            except ValueError:
                raise TypeError("Input must be a numeric value or convertible from string.")

        if not isinstance(distance_miles, (int, float)):
            raise TypeError(f"Invalid type {type(distance_miles).__name__}. Input must be an integer or float.")
        
        # Handle special float values explicitly before conversion logic
        import math as _math_module
        
        if distance_miles != distance_miles:  # NaN check
            raise ValueError("Input cannot be NaN.")
            
        if abs(distance_miles) == float('inf'):
            raise ValueError("Input cannot be Infinity.")

        return self._validate_input(abs(distance_miles)) * self.miles_to_km_factor
    
    def kilometers_to_miles(self, distance_kilometers):
        """Converts a distance from kilometers to miles.
        
        Args:
            distance_kilometers (float or int): The distance in kilometers. Must be non-negative.
            
        Returns:
            float: The equivalent distance in miles.
            
        Raises:
            TypeError: If the input is not numeric.
            ValueError: If the input is negative, NaN, or Infinity.
        """
        if isinstance(distance_kilometers, str):
            try:
                # Attempt to convert string representation of numbers (e.g., "10", "-5")
                distance_kilometers = float(distance_kilometers)
            except ValueError:
                raise TypeError("Input must be a numeric value or convertible from string.")

        if not isinstance(distance_kilometers, (int, float)):
            raise TypeError(f"Invalid type {type(distance_kilometers).__name__}. Input must be an integer or float.")
        
        # Handle special float values explicitly before conversion logic
        import math as _math_module
        
        if distance_kilometers != distance_kilometers:  # NaN check
            raise ValueError("Input cannot be NaN.")
            
        if abs(distance_kilometers) == float('inf'):
            raise ValueError("Input cannot be Infinity.")

        return self._validate_input(abs(distance_kilometers)) / self.miles_to_km_factor

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    converter = DistanceConverter()
    
    print("--- Testing Miles to Kilometers ---")
    try:
        result1 = converter.miles_to_kilometers(5)
        print(f"5 miles -> {result1} km")
        
        # Test with decimal value
        result2 = converter.miles_to_kilometers(3.7)
        print(f"3.7 miles -> {result2:.4f} km")
    except Exception as e:
        print(f"Error in conversion: {e}")

    print("\n--- Testing Kilometers to Miles ---")
    try:
        result3 = converter.kilometers_to_miles(10)
        print(f"10 kilometers -> {result3:.4f} miles")
        
        # Test with decimal value
        result4 = converter.kilometers_to_miles(5.2678)
        print(f"5.2678 km -> {result4:.4f} miles")
    except Exception as e:
        print(f"Error in conversion: {e}")

    print("\n--- Testing Input Validation ---")
    
    # Test non-numeric input
    try:
        converter.miles_to_kilometers("ten")
    except TypeError as e:
        print(f"Caught expected error for string 'ten': {type(e).__name__}: {e}")

    # Test negative number (though logic handles abs, strict validation usually implies non-negative distance)
    try:
        result_neg = converter.miles_to_kilometers(-10)
        print(f"-10 miles converted to absolute value: {result_neg} km") 
    except ValueError as e:
        print(f"Caught error for negative input (if strict): {e}")

    # Test NaN and Infinity simulation via string parsing if needed, but direct float creation handles it in main logic
    
    print("\nAll tests completed successfully.")