class WeightCalculator:
    """A class to perform weight calculations."""

    def calculate_difference(self, weight1: float, weight2: float) -> float:
        """Calculate the difference between two weights.

        Args:
            weight1 (float): The first weight value.
            weight2 (float): The second weight value.

        Returns:
            float: The absolute difference between the two weights.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    
    # Hard-coded sample values as per requirements (no input(), stdin, args, etc.)
    w_a = 75.0
    w_b = 80.5

    difference = calculator.calculate_difference(w_a, w_b)
    print(f"The weight difference is: {difference}")