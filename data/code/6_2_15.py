class WeightCalculator:
    """A class to perform weight-related calculations."""

    def calculate_difference(self, w1: float, w2: float) -> float:
        """Calculate the difference between two weights.

        Args:
            w1 (float): The first weight value.
            w2 (float): The second weight value.

        Returns:
            float: The absolute difference between w1 and w2.
        """
        return abs(w1 - w2)

if __name__ == '__main__':
    # Sample values for testing the WeightCalculator class without user input.
    sample_weight_1 = 50.5
    sample_weight_2 = 47.3

    calculator = WeightCalculator()
    difference = calculator.calculate_difference(sample_weight_1, sample_weight_2)

    print(f"Difference between {sample_weight_1} and {sample_weight_2}: {difference}")