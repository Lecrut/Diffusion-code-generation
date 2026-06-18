class WeightCalculator:
    """A class to calculate weight differences between two values."""

    def __init__(self):
        self._initialized = False

    def initialize(self, unit="kg"):
        """Initialize the calculator with a specific unit of measurement.

        Args:
            unit (str): The unit of measurement for weights (default is "kg").
        
        Raises:
            ValueError: If 'unit' contains invalid characters or is empty.
        """
        if not isinstance(unit, str) or len(unit.strip()) == 0:
            raise ValueError("Unit must be a non-empty string.")

        self.unit = unit.lower().strip()
        # Validate common units to ensure robustness (optional best practice)
        valid_units = ["kg", "lb", "g", "oz"]
        if not any(u in self.unit for u in valid_units):
            print(f"Warning: Unit '{self.unit}' is recognized but may require conversion logic.")

    def calculate_difference(self, weight1, weight2):
        """Calculate the absolute difference between two weights.

        Args:
            weight1 (float or int): The first weight value.
            weight2 (float or int): The second weight value.

        Returns:
            float: The absolute difference between the two weights.
        
        Raises:
            TypeError: If inputs are not numeric.
        """
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise TypeError("Both weight arguments must be numbers.")

        diff = abs(float(weight1) - float(weight2))
        return f"The difference is {diff:.4f} units."

if __name__ == "__main__":
    # Hard-coded sample values to demonstrate functionality without user input.
    
    calculator = WeightCalculator()
    calculator.initialize(unit="kg")

    weight_a = 50.5
    weight_b = 72.3

    result = calculator.calculate_difference(weight_a, weight_b)
    print(result)

    # Additional test case with different units (conceptual demonstration)
    try:
        calc_lbs = WeightCalculator()
        calc_lbs.initialize(unit="lb")
        
        lbs_one = 10.2
        lbs_two = 35.8
        
        result_lbs = calc_lbs.calculate_difference(lbs_one, lbs_two)
        print(result_lbs)
    except Exception as e:
        # This block handles potential unexpected errors gracefully for demonstration
        pass