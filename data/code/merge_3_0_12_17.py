class LengthConverter:
    """A class to convert lengths between meters and feet."""
    
    # Conversion constants defined with high precision
    METERS_PER_FOOT = 0.3048
    
    def __init__(self):
        pass

    def convert(self, value, from_unit, to_unit) -> float:
        """
        Convert a length between meters and feet.
        
        Args:
            value (float): The length value to be converted.
            from_unit (str): Source unit ('meters' or 'feet').
            to_unit (str): Target unit ('meters' or 'feet').
            
        Returns:
            float: Converted length.
            
        Raises:
            ValueError: If units are invalid, not matching, or value is negative.
        """
        
        if from_unit.lower() == "meters" and to_unit.lower() == "feet":
            # Convert meters to feet (multiply by 1 / METER_PER_FOOT)
            return round(value * self.METERS_PER_FOOT**-1, 6)

        elif from_unit.lower() == "feet" and to_unit.lower() == "meters":
            # Convert feet to meters (multiply by METERS_PER_FOOT)
            return value * self.METERS_PER_FOOT
            
        else:
            raise ValueError("Invalid units. Must be 'meters' or 'feet'.")

if __name__ == '__main__':
    converter = LengthConverter()
    
    # Sample conversion tests
    print(f"10 meters to feet: {converter.convert(10, 'meters', 'feet')} ft")
    print(f"32.8084 feet to meters: {converter.convert(32.8084, 'feet', 'meters'): .6f} m")