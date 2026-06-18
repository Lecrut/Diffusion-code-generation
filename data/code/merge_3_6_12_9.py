class WeightCalculator:
    """A class to calculate weight differences between two values."""
    
    def __init__(self):
        self._initialized = False
        
    def initialize(self, value_a, value_b):
        """Initialize the calculator with two weights.
        
        Args:
            value_a (float or int): The first weight value.
            value_b (float or int): The second weight value.
            
        Raises:
            TypeError: If inputs are not numeric.
        """
        if not isinstance(value_a, (int, float)) or not isinstance(value_b, (int, float)):
            raise TypeError("Both values must be numbers.")
        
        self.value_a = value_a
        self.value_b = value_b
        self._initialized = True
        
    def calculate_difference(self):
        """Calculate the absolute difference between the two weights.
        
        Returns:
            float: The absolute difference between value_a and value_b.
            
        Raises:
            ValueError: If the calculator has not been initialized yet.
        """
        if not self._initialized:
            raise ValueError("Calculator must be initialized before calculating differences.")
        
        return abs(self.value_a - self.value_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    calculator = WeightCalculator()
    
    weight_1 = 50.5
    weight_2 = 48.3
    
    try:
        calculator.initialize(weight_1, weight_2)
        difference = calculator.calculate_difference()
        
        print(f"Weight A: {weight_1}")
        print(f"Weight B: {weight_2}")
        print(f"Difference: {difference:.4f} kg")
    except (TypeError, ValueError) as e:
        print(f"Error occurred during calculation: {e}")