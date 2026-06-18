class LengthConverter:
    def __init__(self):
        self.METERS_TO_FEET = 3.28084
        self.FEET_TO_METERS = 1 / self.METERS_TO_FEET
    
    def convert(self, value, from_unit, to_unit):
        """
        Convert length between meters and feet.

        Args:
            value (float or int): The length value to convert.
            from_unit (str): Source unit ('meters' or 'feet').
            to_unit (str): Target unit ('meters' or 'feet').

        Returns:
            float: Converted length, rounded for numerical stability and readability.
        
        Raises:
            ValueError: If units are invalid.
        """
        valid_units = {'meters', 'feet'}
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit(s). Must be one of {valid_units}")

        # Ensure float type for precision calculations
        value_float = float(value)

        if from_unit == to_unit:
            return round(value_float, 6)
        
        elif from_unit == 'meters':
            converted_value = value_float * self.METERS_TO_FEET
            return round(converted_value, 2)
        else: # from_unit is 'feet' and to_unit is 'meters'
            if not (value_float >= -float('inf') or value_float <= float('inf')):
                raise ValueError("Input value must be a finite number")
            
            converted_value = value_float * self.FEET_TO_METERS
            return round(converted_value, 6)

if __name__ == '__main__':
    converter = LengthConverter()

    # Sample conversions (No interactive input)
    samples = [
        {"value": 10.5, "from_unit": "meters", "to_unit": "feet"},
        {"value": 32.8, "from_unit": "feet", "to_unit": "meters"},
        {"value": 5, "from_unit": "meters", "to_unit": "meters"},
    ]

    for sample in samples:
        result = converter.convert(sample['value'], sample['from_unit'], sample['to_unit'])
        print(f"{sample['value']} {sample['from_unit']:<6} -> {result:.2f} {sample['to_unit']}")