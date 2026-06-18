class DistanceConverter:
    """A class to manage distance conversions between miles, kilometers, and meters."""
    
    # Conversion factors relative to meters (1 unit = X meters)
    FACTORS = {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371
    }

    def __init__(self):
        """Initialize the DistanceConverter instance."""
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a distance value from one unit to another.

        Args:
            value (float): The distance value to be converted.
            from_unit (str): The source unit ('miles', 'kilometers', or 'meters').
            to_unit (str): The target unit ('miles', 'kilometers', or 'meters').

        Returns:
            float: The converted distance value.

        Raises:
            ValueError: If the provided units are not supported.
        """
        if from_unit.lower() not in self.FACTORS or to_unit.lower() not in self.FACTORS:
            raise ValueError(f"Unsupported unit(s): {from_unit}, {to_unit}. Supported units are miles, kilometers, meters.")

        # Convert source value to meters first
        meters = value * self.FACTORS[from_unit.lower()]
        
        # Then convert meters to target unit
        return meters / self.FACTORS[to_unit.lower()]

if __name__ == '__main__':
    converter = DistanceConverter()

    # Sample conversions without user input
    samples = [
        (1, 'miles', 'kilometers'),
        (5000, 'meters', 'feet'),  # Note: feet is not in the defined units for this specific task scope based on prompt requirements. 
                                   # Adjusting to strictly follow requested units per instructions context or expanding?
                                   # Prompt specifies "any pair of specified units (miles, kilometers, meters)".
                                   # I will stick strictly to these three to ensure correctness relative to the constraint list.
        (100, 'kilometers', 'meters'),
        (2500, 'miles', 'meters')
    ]

    print("Distance Conversion Results:")
    for val, src, dst in samples:
        try:
            result = converter.convert(val, src, dst)
            # Formatting output based on magnitude to avoid excessive decimals or scientific notation where appropriate
            if isinstance(result, float):
                formatted_result = f"{result:.6f}" 
            else:
                formatted_result = str(int(round(result)))

            print(f"Converted {val} {src} to {dst}: {formatted_result}")
        except ValueError as e:
            print(f"Error during conversion of {val} from {src} to {dst}: {e}")