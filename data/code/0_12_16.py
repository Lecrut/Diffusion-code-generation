class LengthConverter:
    """A class to convert lengths between meters and feet."""

    # Conversion constants defined with high precision
    METERS_PER_FOOT = 0.3048
    
    def __init__(self):
        pass

    def convert(self, value, from_unit, to_unit):
        """
        Converts a length between meters and feet.
        
        Args:
            value (float or int): The numerical value of the length.
            from_unit (str): Source unit ('meters' or 'feet').
            to_unit (str): Target unit ('meters' or 'feet').
            
        Returns:
            float: Converted length as a floating-point number.
            
        Raises:
            ValueError: If units are invalid, source and target are the same, 
                      or if input value is negative where physically impossible for this context.
        """
        
        # Validate inputs
        valid_units = ['meters', 'feet']
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit specified. Must be one of {valid_units}")
            
        if from_unit == to_unit:
            return float(value)

        # Ensure value is non-negative for length conversion context
        if value < 0:
            raise ValueError("Length cannot be negative.")

        try:
            numeric_value = float(value)
        except (TypeError, ValueError):
            raise TypeError(f"Value must be a number. Received {type(value).__name__}.")

        # Conversion logic using the constant METERS_PER_FOOT
        if from_unit == 'meters' and to_unit == 'feet':
            return numeric_value / self.METERS_PER_FOOT
        
        elif from_unit == 'feet' and to_unit == 'meters':
            return numeric_value * self.METERS_PER_FOOT
            
        else:
            # This case is unreachable due to earlier validation, but included for completeness.
            raise ValueError("Conversion direction not supported.")

if __name__ == '__main__':
    converter = LengthConverter()

    # Sample 1: Convert 5 meters to feet
    result_m_to_f = converter.convert(5, 'meters', 'feet')
    
    # Sample 2: Convert 10 feet to meters
    result_f_to_m = converter.convert(10, 'feet', 'meters')

    print(f"5.0 meters is equal to {result_m_to_f:.4f} feet")
    print(f"10.0 feet is equal to {result_f_to_m:.6f} meters")