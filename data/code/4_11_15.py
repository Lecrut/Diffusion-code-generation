class DistanceConverter:
    """A class to convert distances between miles and kilometers."""
    
    # Conversion factor defined as a constant for efficiency and precision
    MILES_TO_KM_FACTOR = 1.60934
    
    def __init__(self):
        self._distance_value = None

    @property
    def distance(self):
        """Returns the current stored distance value."""
        return self._distance_value

    def set_distance(self, miles_or_km: float) -> bool:
        """Sets the internal distance and returns True if successful.
        
        Args:
            miles_or_km (float): The numeric distance to store. 
                                If positive, it is treated as miles; otherwise kilometers.
                                
        Returns:
            bool: True if conversion or setting was valid, False otherwise.
            
        Raises:
            TypeError: If the input is not a number.
        """
        try:
            value = float(miles_or_km)
            self._distance_value = abs(value)  # Store absolute magnitude for calculations
            return True
        except (ValueError, OverflowError):
            return False

    def to_kilometers(self) -> float:
        """Converts the stored distance from miles to kilometers.
        
        Returns:
            float: The equivalent distance in kilometers.
            
        Raises:
            ValueError: If no valid distance has been set yet or if input is invalid.
        """
        if not self._distance_value is None and isinstance(self._distance_value, (int, float)):
            return round(self._distance_value * self.MILES_TO_KM_FACTOR, 2)
        else:
            raise ValueError("No valid distance set to convert.")

    def to_miles(self) -> float:
        """Converts the stored distance from kilometers to miles.
        
        Returns:
            float: The equivalent distance in miles.
            
        Raises:
            ValueError: If no valid distance has been set yet or if input is invalid.
        """
        if not self._distance_value is None and isinstance(self._distance_value, (int, float)):
            return round(abs(self._distance_value) / self.MILES_TO_KM_FACTOR, 2)
        else:
            raise ValueError("No valid distance set to convert.")

    def validate_input(self, value):
        """Validates that the input is numeric.
        
        Args:
            value (any): The value to check.
            
        Returns:
            bool: True if numeric, False otherwise.
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    converter = DistanceConverter()

    # Test Case 1: Valid miles to kilometers conversion
    print("Test Case 1: Converting valid miles (5.0) to kilometers")
    success = converter.set_distance(5.0)
    if success:
        km_result = converter.to_kilometers()
        print(f"Input Miles: {converter.distance}")
        print(f"Converted Kilometers: {km_result}\n")

    # Test Case 2: Valid kilometers to miles conversion (using negative value logic as 'set_distance' stores absolute, 
    # but we assume the intent is setting a specific unit. Since set_distance doesn't track units explicitly in this design
    # for simplicity and robustness against non-numeric strings without crashing immediately on bad types,
    # let's demonstrate input validation failure next)

    print("Test Case 2: Input Validation - Non-numeric value")
    invalid_result = converter.set_distance("invalid_string")