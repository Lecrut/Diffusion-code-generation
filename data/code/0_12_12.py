class LengthConverter:
    """A class to convert lengths between meters and feet."""

    # Conversion constants defined with high precision
    METERS_PER_FOOT = 0.3048
    FEET_PER_METER = 1 / METERS_PER_FOOT

    def _ensure_input_is_number(self, value):
        """Ensure the input value is a number (int or float)."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a numeric type.")
        
        # Handle infinity and NaN cases explicitly for robustness
        import math
        if math.isnan(value) or math.isinf(value):
            return value  # Propagate these as-is

    def convert(self, value, from_unit, to_unit):
        """
        Convert a length between meters and feet.

        Args:
            value (float): The length to be converted.
            from_unit (str): Source unit ('meters' or 'feet').
            to_unit (str): Destination unit ('meters' or 'feet').

        Returns:
            float: The converted length.

        Raises:
            ValueError: If unsupported units are provided.
            TypeError: If the value is not numeric.
        """
        # Validate input types and values
        self._ensure_input_is_number(value)
        
        if from_unit.lower() == to_unit.lower():
            return float(value)

        valid_units = {'meters', 'feet'}
        lower_from = from_unit.lower().strip()
        lower_to = to_unit.lower().strip()

        if lower_from not in valid_units or lower_to not in valid_units:
            raise ValueError(f"Unsupported unit. Must be one of {valid_units}")

        # Normalize units for logic (lowercase, no spaces)
        from_norm = lower_from.strip()
        to_norm = lower_to.strip()

        try:
            value_float = float(value)
        except Exception:
            raise TypeError("Value must be convertible to a float.")

        if from_norm == 'meters' and to_norm == 'feet':
            return round(value_float * self.FEET_PER_METER, 6)
        
        elif from_norm == 'feet' and to_norm == 'meters':
            return round(value_float * self.METERS_PER_FOOT, 6)

        else:
            # This branch handles cases where logic above didn't match (should not be reached with valid inputs)
            raise ValueError("Conversion between meters and feet only.")

if __name__ == '__main__':
    converter = LengthConverter()

    # Sample conversions
    samples = [
        ("10", "meters", "feet"),
        ("3.28084", "feet", "meters"),
        (5, "METERS", "FEET"),  # Case insensitivity test
        ("-5", "feet", "meters")  # Negative value test
    ]

    for val_str, from_u, to_u in samples:
        try:
            result = converter.convert(val_str, from_u, to_u)
            print(f"{val_str} {from_u} -> {result:.6f} {to_u}")
        except Exception as e:
            print(f"Error converting {val_str}: {e}")

    # Additional test for unsupported units
    try:
        converter.convert(10, "meters", "inches")
    except ValueError as ve:
        print(f"Expected error caught: {ve}")