class WeightCalculator:
    """A class to perform weight-related calculations."""

    def calculate_difference(self, weight1: float, weight2: float) -> float:
        """Calculate the absolute difference between two weights.

        Args:
            weight1 (float): The first weight value.
            weight2 (float): The second weight value.

        Returns:
            float: The absolute difference between weight1 and weight2.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    calc = WeightCalculator()
    
    w_a = 50.5
    w_b = 48.3
    
    diff = calc.calculate_difference(w_a, w_b)
    
    print(f"Difference between {w_a} and {w_b}: {diff}")