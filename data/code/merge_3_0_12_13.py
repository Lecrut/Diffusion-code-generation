class LengthConverter:
    """A class to convert lengths between meters and feet."""
    
    # Conversion constants defined once for efficiency and precision
    METERS_TO_FEET = 3.28084
    
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a length value between meters and feet.

        Args:
            value (float): The numeric value to be converted.
            from_unit (str): Source unit ('meters' or 'feet'). Case-insensitive.
            to_unit (str): Target unit ('meters' or 'feet'). Case-insensitive.

        Returns:
            float: The converted length value.

        Raises:
            ValueError: If the input units are not supported.
        """
        # Normalize unit strings for comparison
        from_lower = from_unit.lower().strip()
        to_lower = to_unit.lower().strip()

        if (from_lower != 'meters' and from_lower != 'feet') or \
           (to_lower != 'meters' and to_lower != 'feet'):
            raise ValueError("Unsupported unit. Use 'meters' or 'feet'.")

        # Ensure value is numeric before proceeding with calculation
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be a number, got {type(value).__name__}")

        try:
            converted_value = 0.0
            
            # Convert to meters first as an intermediary step for uniform logic
            meter_value = self._to_meters(value, from_lower)
            
            # Then convert from meters to the target unit
            if to_lower == 'meters':
                return round(meter_value * (1 / 3.28084), 6)  # Round for consistency with input precision expectations
            
            else: # to_unit is feet
                converted_value = meter_value * self.METERS_TO_FEET
                
        except Exception as e:
            raise RuntimeError(f"Conversion failed due to internal error: {e}") from e
        
        return round(converted_value, 6)

    def _to_meters(self, value: float, unit: str) -> float:
        """Internal helper method to convert any input unit to meters."""
        if unit == 'meters':
            return value
        elif unit == 'feet':
            # Standard conversion factor is exactly 1 meter = 3.28084 feet (approx)
            # Using high precision multiplier derived from exact definition where possible
            return value / self.METERS_TO_FEET

if __name__ == '__main__':
    converter = LengthConverter()
    
    # Sample test cases with hard-coded values
    
    # Test case 1: Meters to Feet
    result_m_to_f = converter.convert(5.0, 'meters', 'feet')
    
    # Test case 2: Feet to Meters
    result_f_to_m = converter.convert(16.4, 'feet', 'meters')
    
    # Test case 3: Edge case - Zero value
    zero_result = converter.convert(0.0, 'meters', 'feet')

    print(f"5 meters to feet: {result_m_to_f} ft")
    print(f"16.4 feet to meters: {result_f_to_m} m")
    print(f"0 meters to feet: {zero_result} ft")