class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self):
        self._initialized = True

    def get_weight_difference(self, weight1: float, weight2: float) -> float:
        """
        Calculate the absolute difference between two weights.

        Args:
            weight1 (float): The first weight value.
            weight2 (float): The second weight value.

        Returns:
            float: The absolute difference between the two weights.

        Raises:
            TypeError: If either input is not a number.
        """
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise TypeError("Both inputs must be numeric.")
        
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    calc = WeightCalculator()

    w_a = 50.5
    w_b = 48.3

    diff = calc.get_weight_difference(w_a, w_b)
    
    print(f"Weight difference between {w_a} and {w_b}: {diff}")