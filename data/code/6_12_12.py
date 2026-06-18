class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self, unit='kg'):
        self.unit = unit

    def calculate_difference(self, w1, w2):
        """Calculate the absolute difference between two weights.

        Args:
            w1 (float or int): First weight value.
            w2 (float or int): Second weight value.

        Returns:
            float: The absolute difference between w1 and w2 in the specified unit.
        """
        return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    calculator = WeightCalculator()

    weight_a = 50.5
    weight_b = 73.2

    difference = calculator.calculate_difference(weight_a, weight_b)
    
    print(f"Weight A: {weight_a} {calculator.unit}")
    print(f"Weight B: {weight_b} {calculator.unit}")
    print(f"Difference: {difference:.1f} {calculator.unit}")