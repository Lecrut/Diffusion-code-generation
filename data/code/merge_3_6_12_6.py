class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self, unit='kg'):
        """Initialize with a default unit of measurement.
        
        Args:
            unit (str): The unit for the weights ('kg', 'lb', etc.). Defaults to 'kg'.
        """
        self.unit = unit

    def calculate_difference(self, weight1, weight2):
        """Calculate the absolute difference between two weights.
        
        Args:
            weight1 (float or int): The first weight value.
            weight2 (float or int): The second weight value.
            
        Returns:
            float: The absolute difference between weight1 and weight2.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    calculator = WeightCalculator()

    w_a = 50.5
    w_b = 73.2

    diff = calculator.calculate_difference(w_a, w_b)

    print(f"Weight difference between {w_a} and {w_b}: {diff}")