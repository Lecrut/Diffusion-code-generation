class LengthConverter:
    """A class to convert lengths between meters and feet."""

    # Conversion constants defined with high precision
    METERS_PER_FOOT = 0.3048
    FEET_PER_METER = 1 / METERS_PER_FOOT

    def convert(self, value, from_unit, to_unit):
        """
        Convert a length between meters and feet.

        Args:
            value (float or int): The numerical value of the length.
            from_unit (str): Source unit ('meters' or 'feet'). Case-insensitive.
            to_unit (str): Target unit ('meters' or 'feet'). Case-insensitive.

        Returns:
            float: Converted length as a floating-point number.

        Raises:
            ValueError: If the input units are not supported.
        """
        # Normalize input strings for comparison
        from_unit_lower = from_unit.lower().strip()
        to_unit_lower = to_unit.lower().strip()

        if from_unit_lower == 'meters':
            source_value_meters = value
        elif from_unit_lower == 'feet':
            source_value_meters = value * self.METERS_PER_FOOT
        else:
            raise ValueError(f"Unsupported unit for conversion: {from_unit}")

        if to_unit_lower == 'meters':
            return round(source_value_meters, 10)
        elif to_unit_lower == 'feet':
            result_feet = source_value_meters / self.METERS_PER_FOOT
            # Round to avoid floating point artifacts (e.g., 2.9999999 -> 3)
            return round(result_feet, 10)
        else:
            raise ValueError(f"Unsupported unit for conversion: {to_unit}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without interactive input
    converter = LengthConverter()

    test_cases = [
        (25, 'meters', 'feet'),      # 25 meters -> feet
        (100.34, 'feet', 'meters'), # 100.34 feet -> meters
        (1, 'meters', 'meters'),     # Identity conversion for meters
        (6, 'feet', 'feet'),         # Identity conversion for feet
    ]

    print("Length Conversion Results:")
    for value, from_u, to_u in test_cases:
        converted = converter.convert(value, from_u, to_u)
        unit_map = {'meters': 'm', 'feet': 'ft'}
        print(f"{value} {from_u} is equal to {converted:.6f} {unit_map[to_u]}")

    # Additional specific example: 10 feet should be exactly 3.048 meters
    result = converter.convert(10, 'feet', 'meters')
    print(f"\nVerification (10 ft -> m): Expected 3.048, Got {result}")