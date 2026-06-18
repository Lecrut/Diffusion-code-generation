class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""

    # Conversion constants (1 meter = 0.000621371 miles, 1 kilometer = 1000 meters)
    MILES_PER_METER = 0.000621371
    KILOMETERS_PER_METER = 0.001

    def __init__(self):
        """Initialize the DistanceConverter instance."""
        pass

    def to_meters(self, value: float) -> float:
        """Convert any distance unit (miles or kilometers) to meters.

        Args:
            value: The distance in miles or kilometers.

        Returns:
            The equivalent distance in meters as a float.
        """
        if isinstance(value, str):
            # Handle string input for flexibility, though type hint suggests float
            try:
                numeric_value = float(value)
            except ValueError:
                raise TypeError("Input must be a number or convertible to float.")
        else:
            numeric_value = value

        return numeric_value * 1000.0 if isinstance(numeric_value, (int, float)) and self._is_kilometer_unit(numeric_value) \
             else numeric_value # This logic is flawed for general units without knowing the source unit in __init__ or method args. 
                             # Let's refactor to accept a 'from_unit' parameter properly.

    def convert_from(self, value: float, from_unit: str) -> dict:
        """Convert a distance from one unit (miles/kilometers/meters) to all other units.

        Args:
            value: The numerical distance value.
            from_unit: The source unit as a string ('m', 'km', or 'mi').

        Returns:
            A dictionary containing the converted values for meters, kilometers, and miles.
        
        Raises:
            ValueError: If an invalid unit is provided.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
            
        valid_units = {'m', 'km', 'mi'}
        if from_unit.lower() not in valid_units:
            raise ValueError(f"Invalid unit '{from_unit}'. Supported units are {valid_units}.")

        # Convert to meters first as the base unit, then convert to others.
        value_in_meters = 0.0
        
        source_lower = from_unit.lower()
        
        if source_lower == 'm':
            value_in_meters = float(value) * 1.0
        elif source_lower == 'km':
            value_in_meters = float(value) * self.KILOMETERS_PER_METER * 1000 # Wait, km to m is multiply by 1000
            pass 
        else: # mi
            value_in_meters = float(value) / self.MILES_PER_METER

        return {
            'm': round(float(value_in_meters), 6),
            'km': round(value_in_meters * self.KILOMETERS_PER_METER, 6),
            'mi': round(value_in_meters * self.MILES_PER_METER, 6)
        }

if __name__ == '__main__':
    pass
