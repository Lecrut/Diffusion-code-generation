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
            value (float): The numerical value of the length.
            from_unit (str): The unit to convert from ('meters' or 'feet').
            to_unit (str): The unit to convert to ('meters' or 'feet').

        Returns:
            float: The converted length.

        Raises:
            ValueError: If the input units are invalid.
        """
        valid_units = {'meters', 'feet'}
        
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit(s). Must be one of {valid_units}")

        # Normalize value based on source unit, then convert to target unit
        if from_unit == 'meters':
            meters = value
        elif from_unit == 'feet':
            meters = value * self.METERS_PER_FOOT
        
        # Convert to desired output unit using the pre-calculated constant for efficiency
        return meters * (self.FEET_PER_METER if to_unit == 'feet' else 1.0)

if __name__ == '__main__':
    converter = LengthConverter()

    # Sample conversions with hard-coded values
    sample_tests = [
        ("meters", "feet", 5),           # Convert 5 meters to feet
        ("feet", "meters", 10.936),      # Convert ~36 feet (approx) to meters
        ("meters", "meters", 20.5),      # Identity conversion for precision check
    ]

    print("Length Conversion Results:")
    for from_u, to_u, val in sample_tests:
        result = converter.convert(val, from_u, to_u)
        print(f"{val} {from_u} -> {result:.6f} {to_u}")