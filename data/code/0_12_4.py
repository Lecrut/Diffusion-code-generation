class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        """
        Converts a length between meters and feet.
        
        Args:
            value (float): The numerical length value.
            from_unit (str): Source unit ('meters' or 'feet').
            to_unit (str): Target unit ('meters' or 'feet').
            
        Returns:
            float: Converted length.
            
        Raises:
            ValueError: If units are invalid or source and target are the same.
        """
        valid_units = {'meters', 'feet'}
        
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit provided. Must be one of {valid_units}")
        
        if from_unit == to_unit:
            return value
        
        # Conversion factor: 1 meter = 3.28084 feet (standard international definition)
        METERS_TO_FEET_FACTOR = 3.28084

        if from_unit == 'meters' and to_unit == 'feet':
            return round(value * METERS_TO_FEET_FACTOR, 6)
        
        elif from_unit == 'feet' and to_unit == 'meters':
            # Inverse factor: 1 foot = 0.3048 meters (exact definition)
            FEET_TO_METERS_FACTOR = 0.3048
            return round(value * FEET_TO_METERS_FACTOR, 6)

        else:
            raise ValueError("Conversion direction not supported.")

if __name__ == '__main__':
    converter = LengthConverter()
    
    # Sample conversions with hard-coded values
    sample_cases = [
        {'value': 10.5, 'from_unit': 'meters', 'to_unit': 'feet'},
        {'value': 20.3, 'from_unit': 'feet', 'to_unit': 'meters'},
        {'value': 1, 'from_unit': 'meters', 'to_unit': 'meters'},
    ]

    for case in sample_cases:
        result = converter.convert(
            value=case['value'], 
            from_unit=case['from_unit'], 
            to_unit=case['to_unit']
        )
        print(f"{case['value']} {case['from_unit']} -> {result} {case['to_unit']}")