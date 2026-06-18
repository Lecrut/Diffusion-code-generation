class LengthConverter:
    """A class to convert lengths between meters and feet."""
    
    def __init__(self):
        # Constants defined with high precision (1 meter = 3.28084 feet)
        self.METER_TO_FEET_FACTOR = 3.28084

    def convert(self, value, from_unit, to_unit):
        """
        Convert a length between meters and feet.

        Args:
            value (float or int): The length value to convert.
            from_unit (str): Source unit ('meters' or 'feet'). Case-insensitive.
            to_unit (str): Target unit ('meters' or 'feet'). Case-insensitive.

        Returns:
            float: The converted length.

        Raises:
            ValueError: If unsupported units are provided.
        """
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()

        valid_units = {'meters', 'feet'}
        
        if not (from_unit_lower in valid_units and to_unit_lower in valid_units):
            raise ValueError(f"Unsupported units. Valid options: {valid_units}")

        # Convert meters to feet factor, convert feet back to meters by dividing
        if from_unit_lower == 'meters' and to_unit_lower == 'feet':
            return value * self.METER_TO_FEET_FACTOR
        
        elif from_unit_lower == 'feet' and to_unit_lower == 'meters':
            # 1 foot = 0.3048 meters exactly (inverse of the factor used above for precision)
            return value / self.METER_TO_FEET_FACTOR

        else:
            raise ValueError("Input units are not supported.")

if __name__ == '__main__':
    converter = LengthConverter()
    
    # Sample 1: Convert 5 meters to feet
    result_m_to_f = converter.convert(5, 'meters', 'feet')

    # Sample 2: Convert 30.48 feet back to meters (should be exactly 1 meter)
    result_f_to_m = converter.convert(30.48, 'feet', 'meters')

    print(f"{5} meters is {result_m_to_f:.6f} feet.")
    print(f"{30.48} feet is {result_f_to_m:.10f} meters.")