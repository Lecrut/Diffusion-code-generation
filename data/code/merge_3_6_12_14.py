class WeightCalculator:
    """A class to handle weight calculations."""

    def calculate_weight_difference(self, w1: float, w2: float) -> float:
        """Calculate the absolute difference between two weights.

        Args:
            w1 (float): The first weight value.
            w2 (float): The second weight value.

        Returns:
            float: The absolute difference between w1 and w2.
        """
        return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    sample_weight_1 = 50.0
    sample_weight_2 = 75.5

    calculator = WeightCalculator()
    difference = calculator.calculate_weight_difference(sample_weight_1, sample_weight_2)

    print(f"Weight 1: {sample_weight_1}")
    print(f"Weight 2: {sample_weight_2}")
    print(f"Difference: {difference}")