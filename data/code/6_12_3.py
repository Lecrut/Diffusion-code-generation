class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self):
        self._initialized = False

    def initialize(self, unit='kg'):
        """Initialize the calculator with a specific unit.

        Args:
            unit (str): The unit of measurement for weights (default is 'kg').
        
        Raises:
            ValueError: If an invalid weight value or non-numeric input is provided during initialization logic if extended later.
        """
        self.unit = unit
        # In a more complex design, we might store reference values here.

    def calculate_difference(self, w1, w2):
        """Calculate the absolute difference between two weights.

        Args:
            w1 (float or int): The first weight value.
            w2 (float or int): The second weight value.

        Returns:
            float: The absolute difference between w1 and w2 in the specified unit.

        Raises:
            TypeError: If either input is not a number.
        """
        if not isinstance(w1, (int, float)) or not isinstance(w2, (int, float)):
            raise TypeError("Both weights must be numeric values.")
        
        return abs(float(w1) - float(w2))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    calculator = WeightCalculator()

    weight_a = 50.5
    weight_b = 73.2
    
    difference = calculator.calculate_difference(weight_a, weight_b)
    
    print(f"Weight A: {weight_a} units")
    print(f"Weight B: {weight_b} units")
    print(f"Difference: {difference:.1f} units")