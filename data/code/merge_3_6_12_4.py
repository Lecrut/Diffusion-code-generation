class WeightCalculator:
    """A class designed to calculate weight differences between two values."""

    def __init__(self, unit="kg"):
        self.unit = unit.capitalize() if isinstance(unit, str) else "Kg"

    def get_difference(self, value1, value2):
        """Calculates the absolute difference between two weights.
        
        Args:
            value1 (float or int): The first weight value.
            value2 (float or int): The second weight value.
            
        Returns:
            float: The absolute difference between the two weights, 
                   appended with the unit string.
        """
        diff = abs(value1 - value2)
        return f"{diff}{self.unit}"

if __name__ == "__main__":
    # Hard-coded sample values to ensure no external input or dependencies are needed.
    calc = WeightCalculator()

    weight_a = 50.5
    weight_b = 73.2

    result = calc.get_difference(weight_a, weight_b)
    
    print(f"Weight Difference: {result}")