class LengthConverter:
    def __init__(self):
        # Conversion factor from meters to feet is 3.28084
        self.meters_to_feet = 3.28084
    
    def convert(self, value, from_unit, to_unit):
        """
        Converts a length between meters and feet.

        Args:
            value (float): The length value to convert.
            from_unit (str): Source unit ('m' for meter or 'ft' for foot).
            to_unit (str): Target unit ('m' for meter or 'ft' for foot).

        Returns:
            float: Converted length.

        Raises:
            ValueError: If input units are invalid or source and target units match.
        """
        # Normalize inputs to lowercase for case-insensitive comparison
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if not (from_unit in ['m', 'ft'] and to_unit in ['m', 'ft']):
            raise ValueError("Invalid units. Use 'm' or 'ft'.")
        
        # If start and end unit are the same, return original value
        if from_unit == to_unit:
            return float(value)

        try:
            num = float(value)
        except (ValueError, TypeError):
            raise ValueError("Input value must be a number.")

        # Define conversion paths based on input units
        if from_unit == 'm' and to_unit == 'ft':
            return round(num * self.meters_to_feet, 6)
        
        elif from_unit == 'ft' and to_unit == 'm':
            factor = 1 / self.meters_to_feet  # Approximately 0.3048
            result = num * factor
            
            # To ensure mathematical precision for division, we can multiply by a precise fraction or use high-precision float if available. 
            # Standard IEEE754 double precision is usually sufficient here given the constant's accuracy requirement in typical engineering contexts unless scientific applications are specified.
            return round(result, 6)

        else:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}.")

if __name__ == '__main__':
    # Hard-coded sample values for testing the converter logic
    
    lc = LengthConverter()
    
    test_cases = [
        ('meters', 10, 'feet'),       # 10 meters -> feet
        ('feet', 3.28084, 'meters'), # ~3.28 foot -> meters (should be approx 1)
        ('meters', 5, 'feet'),         # Simple conversion
    ]

    for from_unit_name, value, to_unit_name in test_cases:
        try:
            converted_value = lc.convert(value, from_unit_name, to_unit_name)
            print(f"Converted {value} {from_unit_name} to {converted_value}")
        except ValueError as e:
            print(f"Error during conversion for input {value}: {e}")