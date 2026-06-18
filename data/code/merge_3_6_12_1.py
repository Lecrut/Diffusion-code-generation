class WeightCalculator:
    """A class to calculate weight differences between any two weights."""

    def __init__(self):
        self._history = []  # Internal state to track calculations (optional best practice)

    def get_weight_difference(self, weight1: float | int, weight2: float | int) -> float:
        """Calculate the absolute difference between two weights.

        Args:
            weight1: The first weight value.
            weight2: The second weight value.

        Returns:
            The absolute difference between the two weights as a float.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    calculator = WeightCalculator()

    # Sample inputs
    w_a = 50.75
    w_b = 48.30

    diff = calculator.get_weight_difference(w_a, w_b)

    print(f"Weight A: {w_a}")
    print(f"Weight B: {w_b}")
    print(f"Difference: {diff:.2f} kg")