class WeightCalculator:
    """A class to perform weight-related calculations."""

    def calculate_difference(self, weight1: float, weight2: float) -> float:
        """Calculate the absolute difference between two weights.

        Args:
            weight1 (float): The first weight value.
            weight2 (float): The second weight value.

        Returns:
            float: The absolute difference between the two weights.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_weight_a = 50.5
    sample_weight_b = 48.7

    calculator = WeightCalculator()
    difference = calculator.calculate_difference(sample_weight_a, sample_weight_b)

    print(f"The difference between {sample_weight_a} and {sample_weight_b} is: {difference}")