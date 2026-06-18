import math

class DistanceConverter:
    """A class to convert distances between miles and kilometers with input validation."""
    
    # Conversion constant defined by international standards (1 mile = 1609.344 meters)
    MILES_TO_METERS_PER_MILE = 1609.344
    
    def __init__(self):
        """Initialize the DistanceConverter instance with default settings."""
        pass

    def _validate_input(self, value):
        """Validate that the input is a numeric type (int or float)."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Input must be a number, got {type(value).__name__}")
        
        # Check for NaN and Infinity cases to ensure mathematical soundness
        if math.isnan(float(value)) or math.isinf(float(value)):
            raise ValueError("Input cannot contain non-finite values (NaN or infinity).")

    def _convert_miles_to_kilometers(self, miles):
        """Convert distance from miles to kilometers."""
        self._validate_input(miles)
        
        # Convert meters per mile to kilometers per mile (divide by 1000)
        km_per_mile = self.MILES_TO_METERS_PER_MILE / 1000.0
        
        return miles * km_per_mile

    def _convert_kilometers_to_miles(self, kilometers):
        """Convert distance from kilometers to miles."""
        self._validate_input(kilometers)
        
        # Convert meters per mile back to miles (multiply by 1/1609.344 or divide by km_per_mile)
        return kilometers / km_per_mile

    def convert(self, value, from_unit):
        """
        Main method to convert distance accurately between miles and kilometers.
        
        Args:
            value (int|float): The numerical distance value to be converted.
            from_unit (str): Source unit of measurement ('miles' or 'kilometers').
            
        Returns:
            float: Converted distance in the target unit.
            
        Raises:
            ValueError: If input is not numeric, contains non-finite values, 
                      or if an invalid source unit is provided.
            TypeError: If the value argument is of an unsupported type.
        """
        self._validate_input(value)

        # Validate units to ensure mathematical soundness and prevent runtime errors
        valid_units = {'miles', 'kilometers'}
        if from_unit not in valid_units:
            raise ValueError(f"Unsupported unit '{from_unit}'. Must be one of {valid_units}")

        try:
            if from_unit == 'miles':
                return self._convert_miles_to_kilometers(value)
            elif from_unit == 'kilometers':
                return self._convert_kilometers_to_miles(value)
        except (ValueError, TypeError):
            raise

if __name__ == '__main__':
    pass
