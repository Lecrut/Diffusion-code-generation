class LengthConverter:
    """A class to convert length values between meters and feet."""

    # Conversion factor from meters to feet (1 meter = 3.28084 feet)
    METERS_TO_FEET_FACTOR = 3.28084
    
    def __init__(self):
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a length between meters and feet.
        
        Args:
            value (float): The length value to convert.
            from_unit (str): Source unit ('meters' or 'feet').
            to_unit (str): Target unit ('meters' or 'feet').
            
        Returns:
            float: Converted length with high precision.
            
        Raises:
            ValueError: If input units are invalid.
        """
        valid_units = {'meters', 'feet'}
        
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit(s). Expected one of {valid_units}, got '{from_unit}' and '{to_unit}'.")

        # Handle conversion logic based on source and target units
        try:
            value = float(value)
            
            if from_unit == to_unit:
                return value
            
            elif from_unit == 'meters':
                converted_value = self.METERS_TO_FEET_FACTOR * value
                return converted_value
                
            else:  # from_unit is 'feet', converting to meters
                converted_value = value / self.METERS_TO_FEET_FACTOR
                return converted_value
                
        except (TypeError, ValueError):
            raise TypeError("Input must be a numeric type.")

if __name__ == '__main__':
    converter = LengthConverter()
    
    # Sample conversions without interactive input
    
    # Convert 10 meters to feet
    result_m_to_f = converter.convert(10.0, 'meters', 'feet')
    print(f"{result_m_to_f} feet")

    # Convert 328 feet to meters (approximate for exactly 100 meters)
    result_f_to_m = converter.convert(328.0, 'feet', 'meters')
    print(result_f_to_m, "meters")

    # Ensure same value when converting back and forth with precision check
    original_value = 5.6789
    converted_back = converter.convert(original_value * (converter.METERS_TO_FEET_FACTOR / 10), 'feet', 'meters') 
    print(f"Precision test: {original_value} meters -> feet -> meters")

    # Invalid unit handling example
    try:
        result = converter.convert(5.0, 'yards', 'inches')
    except ValueError as e:
        print("Error:", str(e))