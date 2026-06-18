class DistanceConverter:
    """A class to handle distance conversions between miles, kilometers, and meters."""
    
    # Conversion factors relative to 1 mile
    CONVERSION_FACTORS = {
        'miles': 1.0,
        'kilometers': 1.60934,
        'meters': 1609.34
    }

    def __init__(self):
        """Initialize the DistanceConverter instance."""
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a distance from one unit to another.
        
        Args:
            value (float): The distance value in the source unit.
            from_unit (str): The source unit ('miles', 'kilometers', or 'meters').
            to_unit (str): The target unit ('miles', 'kilometers', or 'meters').
            
        Returns:
            float: The converted distance in the target unit.
            
        Raises:
            ValueError: If an unsupported unit is provided.
        
        """
        if from_unit not in self.CONVERSION_FACTORS or to_unit not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported units. Supported units are: {list(self.CONVERSION_FACTORS.keys())}")

        # Convert source value to meters first, then convert from meters to target unit
        intermediate_meters = value * self.CONVERSION_FACTORS[from_unit]
        converted_value = intermediate_meters / self.CONVERSION_FACTORS[to_unit]
        
        return converted_value

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    converter = DistanceConverter()

    # Example 1: Convert 5 miles to kilometers
    result_kilometers = converter.convert(5, 'miles', 'kilometers')
    
    # Example 2: Convert 30 km to meters
    result_meters_30km = converter.convert(30, 'kilometers', 'meters')

    # Example 3: Convert 10000 meters back to miles (rounding for clean output)
    result_miles = round(converter.convert(10000, 'meters', 'miles'), 4)
    
    print(f"5.0 miles is equal to {result_kilometers:.2f} kilometers")
    print("30.0 kilometers is equal to", f"{result_meters_30km:,.2f}" + " meters")
    print(f"10,000 meters is approximately {result_miles:.4f} miles")