class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self):
        self._initialized = False

    @property
    def is_initialized(self) -> bool:
        return self._initialized

    def initialize_weights(self, w1: float, w2: float) -> None:
        """Initialize the calculator with two weight values.

        Args:
            w1 (float): The first weight value.
            w2 (float): The second weight value.

        Raises:
            TypeError: If inputs are not numeric floats or ints.
        """
        if not isinstance(w1, (int, float)) or not isinstance(w2, (int, float)):
            raise TypeError("Both weights must be numbers.")

        self.w1 = w1
        self.w2 = w2
        self._initialized = True

    def calculate_difference(self) -> float:
        """Calculate the absolute difference between the two initialized weights.

        Returns:
            float: The absolute difference |w1 - w2|.

        Raises:
            ValueError: If no weights have been initialized yet.
        """
        if not self._initialized:
            raise ValueError("No weights initialized in WeightCalculator.")
        
        return abs(self.w1 - self.w2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    calculator = WeightCalculator()

    try:
        w_a = 50.5
        w_b = 48.3
        
        calculator.initialize_weights(w_a, w_b)
        
        difference = calculator.calculate_difference()
        
        print(f"Weight A: {w_a}")
        print(f"Weight B: {w_b}")
        print(f"Difference: {difference}")
    except Exception as e:
        print(f"Error occurred during calculation: {e}")