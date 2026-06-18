class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self):
        self._weight_difference = 0.0

    @staticmethod
    def get_weight_difference(weight_a, weight_b):
        """Calculate the absolute difference between two weights.

        Args:
            weight_a (float or int): The first weight value.
            weight_b (float or int): The second weight value.

        Returns:
            float: The absolute difference between the two weights.
        """
        return abs(weight_a - weight_b)

if __name__ == '__main__':
    calculator = WeightCalculator()

    # Hard-coded sample values for testing
    weight1 = 75.0
    weight2 = 82.5

    difference = calculator.get_weight_difference(weight1, weight2)

    print(f"Weight Difference: {difference}")