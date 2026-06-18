class DistanceConverter:
    """A class to manage distance conversions between miles, kilometers, and meters."""
    
    # Conversion factors relative to one meter (1 unit = X meters)
    FACTORS = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.344,
    }

    def __init__(self):
        """Initialize the DistanceConverter instance."""
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a distance value from one unit to another.

        Args:
            value (float): The distance value to convert.
            from_unit (str): The source unit ('miles', 'kilometers', or 'meters').
            to_unit (str): The target unit ('miles', 'kilometers', or 'meters').

        Returns:
            float: The converted distance.

        Raises:
            ValueError: If the units are invalid or match.
        """
        if from_unit not in self.FACTORS or to_unit not in self.FACTORS:
            raise ValueError(f"Invalid unit provided. Supported units: {list(self.FACTORS.keys())}")
        
        # Ensure we don't convert a value to the same unit (though mathematically it works, 
        # this check improves logic clarity as per task requirements for distinct pairs)
        if from_unit == to_unit:
            return float(value)

        # Convert source to meters first, then target units
        meters = value * self.FACTORS[from_unit]
        result_meters = meters / self.FACTORS[to_unit]
        
        return round(result_meters, 2)

if __name__ == '__main__':
    converter = DistanceConverter()

    # Sample conversions without user input
    print(f"Converting {10} miles to kilometers: {converter.convert(10, 'miles', 'kilometers')}")
    print(f"Converting {5.2} kilometers to meters: {converter.convert(5.2, 'kilometers', 'meters')}")
    print(f"Converting {34876} meters to miles: {converter.convert(34876, 'meters', 'miles')}")