class LengthConverter:
    """A class to convert lengths between meters and feet."""

    # Conversion constants defined with high precision
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 0.3048

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
            ValueError: If the units are invalid or if both input and output units are the same.
        """
        valid_units = {'meters', 'feet'}
        
        # Validate inputs
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit provided. Must be one of {valid_units}")
        
        if from_unit == to_unit:
            return value

        # Perform conversion based on direction
        if from_unit == 'meters' and to_unit == 'feet':
            return self.METERS_TO_FEET * value
        
        elif from_unit == 'feet' and to_unit == 'meters':
            return self.FEET_TO_METERS * value

        else:
            # This case should theoretically be caught by the if/elif above, 
            # but kept for structural completeness.
            raise ValueError("Conversion direction not supported.")

if __name__ == '__main__':
    converter = LengthConverter()

    # Sample 1: Convert 5 meters to feet
    result_m_to_f = converter.convert(5, 'meters', 'feet')
    
    # Sample 2: Convert 100 feet to meters
    result_f_to_m = converter.convert(100, 'feet', 'meters')

    print(f"{result_m_to_f} {converter.METERS_TO_FEET}")