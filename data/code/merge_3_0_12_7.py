class LengthConverter:
    def __init__(self):
        """Initialize the converter with standard conversion factors."""
        # 1 meter = 3.28084 feet (approximate precise value)
        self.meter_to_feet_factor = 3.28084
        
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a length between meters and feet.

        Args:
            value (float): The numerical value of the length.
            from_unit (str): Source unit ('m' for meter or 'ft' for foot).
            to_unit (str): Target unit ('m' for meter or 'ft' for foot).

        Returns:
            float: Converted length if units are valid, otherwise 0.0.
        
        Raises:
            ValueError: If input value is not numeric or units are invalid.
            TypeError: If any argument type is incorrect.
        """
        # Validate types and values
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
            
        valid_units = {'m': 'meter', 'ft': 'foot'}
        
        source_key = from_unit.lower()
        target_key = to_unit.lower()
        
        # Check for invalid unit characters or unsupported units beyond m/ft
        if not (source_key in ['m', 'ft'] and target_key in ['m', 'ft']):
            raise ValueError("Units must be either 'm' (meter) or 'ft' (foot).")

        try:
            value = float(value)
            
            # Handle zero conversion directly to avoid floating point issues early on
            if abs(value) < 1e-9:
                return float(0.0)
                
            # Perform conversion logic based on source and target units
            if from_unit == 'm' and to_unit == 'ft':
                converted_value = value * self.meter_to_feet_factor
            elif from_unit == 'ft' and to_unit == 'm':
                converted_value = value / self.meter_to_feet_factor
            else:
                # Same units (e.g., m to m or ft to ft) - return original value as float precision is maintained
                return float(value)

            return converted_value
            
        except OverflowError:
            raise ValueError("Value too large for conversion.")

if __name__ == '__main__':
    converter = LengthConverter()
    
    # Sample 1: Convert specific meters to feet with high precision expectation
    sample_1_meters = 5.0
    result_1 = converter.convert(sample_1_meters, 'm', 'ft')
    print(f"Converted {sample_1_meters} m to ft: {result_1}")

    # Sample 2: Convert specific feet back to meters
    sample_2_feet = 30.0
    result_2 = converter.convert(sample_2_feet, 'ft', 'm')
    print(f"Converted {sample_2_feet} ft to m: {result_2}")

    # Sample 3: Same unit conversion (identity test)
    sample_3_meters = 10.5
    result_3_same_unit = converter.convert(sample_3_meters, 'm', 'm')
    print(f"Converted {sample_3_meters} m to same unit (m): {result_3_same_unit}")

    # Sample 4: Edge case very small number
    sample_4_small = 0.0125
    result_4 = converter.convert(sample_4_small, 'ft', 'm')
    print(f"Converted {sample_4_small} ft to m (approx): {result_4}")