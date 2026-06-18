class LengthConverter:
    """A class to convert lengths between meters and feet."""

    # Conversion constants defined with high precision
    METERS_PER_FOOT = 0.3048
    FEET_PER_METER = 1 / METERS_PER_FOOT

    def __init__(self):
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a length between meters and feet.

        Args:
            value (float): The length value to be converted.
            from_unit (str): The source unit ('meters' or 'feet').
            to_unit (str): The target unit ('meters' or 'feet').

        Returns:
            float: The converted length.

        Raises:
            ValueError: If an invalid unit is provided.
        """
        valid_units = {'meters', 'feet'}
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid units provided. Must be one of {valid_units}")

        # Normalize input value and source unit for consistent logic flow
        normalized_value = 0.0
        
        # If converting FROM meters TO feet, multiply by conversion factor directly
        if from_unit == 'meters' and to_unit == 'feet':
            return round(value * FEET_PER_METER, 6)
        
        # If converting FROM feet TO meters, divide by conversion factor (or multiply reciprocal)
        elif from_unit == 'feet' and to_unit == 'meters':
            return round(value / METERS_PER_FOOT, 6)

        raise ValueError("Conversion only supported between meters and feet.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    
    converter = LengthConverter()
    
    # Sample conversions
    samples = [
        ('meters', 'feet'),   # 10 meters to feet
        ('feet', 'meters'),   # 3.28 feet to meters (approx 1 meter)
        ('meters', 'feet'),   # 5 meters to feet
    ]