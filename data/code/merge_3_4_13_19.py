class DistanceConverter:
    """A class to manage distance conversions between miles, kilometers, and meters."""
    
    # Conversion factors relative to 1 meter
    METERS_PER_MILE = 1609.34
    METERS_PER_KILOMETER = 1000

    def __init__(self):
        """Initialize the DistanceConverter with standard conversion constants."""
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a distance value from one unit to another.
        
        Args:
            value (float): The distance value to convert.
            from_unit (str): The source unit ('miles', 'kilometers', or 'meters').
            to_unit (str): The target unit ('miles', 'kilometers', or 'meters').
            
        Returns:
            float: The converted distance in the target unit.
            
        Raises:
            ValueError: If an invalid unit is provided.
        """
        valid_units = ['miles', 'kilometers', 'meters']
        
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid units provided. Must be one of {valid_units}")

        # Convert source unit to meters first, then convert meters to target unit
        value_in_meters = self._to_base(value, from_unit)
        
        return self._from_base(value_in_meters, to_unit)

    def _to_base(self, value: float, unit: str) -> float:
        """Convert a given distance in the specified unit to meters."""
        if unit == 'miles':
            return value * self.METERS_PER_MILE
        elif unit == 'kilometers':
            return value * self.METERS_PER_KILOMETER
        else:  # meters
            return value

    def _from_base(self, value_in_meters: float, target_unit: str) -> float:
        """Convert a distance in meters to the specified target unit."""
        if target_unit == 'miles':
            return value_in_meters / self.METERS_PER_MILE
        elif target_unit == 'kilometers':
            return value_in_meters / self.METERS_PER_KILOMETER
        else:  # meters
            return value

if __name__ == '__main__':
    # Sample usage block with hard-coded values
    converter = DistanceConverter()

    print("Distance Conversion Examples:")
    
    # Example 1: Miles to Kilometers
    result_1 = converter.convert(5.0, 'miles', 'kilometers')
    print(f"{result_1:.2f} miles is {result_1:.4f} kilometers")

    # Example 2: Meters to Miles
    result_2 = converter.convert(160934.0, 'meters', 'miles')
    print(f"{result_2:.5f} meters is approximately equal to the input in miles (roundtrip check)")

    # Example 3: Kilometers to Meters
    result_3 = converter.convert(10.0, 'kilometers', 'meters')
    print(f"10 kilometers equals {result_3:.2f} meters")