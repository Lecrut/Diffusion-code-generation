class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self):
        self._history = []  # Internal list to store calculation history (optional feature)

    def get_weight_difference(self, value1: float, value2: float) -> float:
        """
        Calculate the absolute difference between two weights.

        Args:
            value1 (float): The first weight value.
            value2 (float): The second weight value.

        Returns:
            float: The absolute difference between value1 and value2.
        """
        return abs(value1 - value2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    calculator = WeightCalculator()

    weight_a = 50.5
    weight_b = 48.3

    diff = calculator.get_weight_difference(weight_a, weight_b)

    print(f"Weight A: {weight_a}")
    print(f"Weight B: {weight_b}")
    print(f"Difference: {diff}")