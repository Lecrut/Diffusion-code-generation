class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self):
        """Initialize the calculator with no dependencies."""
        pass

    def get_weight_difference(self, weight1: float, weight2: float) -> float:
        """
        Calculate the absolute difference between two weights.

        Args:
            weight1 (float): The first weight value.
            weight2 (float): The second weight value.

        Returns:
            float: The absolute difference between the two weights.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    calculator = WeightCalculator()

    w_a = 50.5
    w_b = 48.2

    difference = calculator.get_weight_difference(w_a, w_b)

    print(f"Weight A: {w_a}")
    print(f"Weight B: {w_b}")
    print(f"Difference: {difference}")