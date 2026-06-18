class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def difference(self, w1: float, w2: float) -> float:
        """Calculate and return the absolute difference between two weights.

        Args:
            w1 (float): The first weight value.
            w2 (float): The second weight value.

        Returns:
            float: The absolute difference between w1 and w2.
        """
        return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    calculator = WeightCalculator()
    
    # Sample weights in kilograms
    weight_a = 75.0
    weight_b = 80.5

    diff = calculator.difference(weight_a, weight_b)
    print(f"The difference between {weight_a} kg and {weight_b} kg is: {diff:.2f} kg")