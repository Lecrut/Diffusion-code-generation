class WeightCalculator:
    """A class to handle weight calculations."""

    def calculate_difference(self, weight1: float, weight2: float) -> float:
        """Calculate the absolute difference between two weights.
        
        Args:
            weight1 (float): The first weight value.
            weight2 (float): The second weight value.
            
        Returns:
            float: The absolute difference between the two weights.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    sample_weight_1 = 50.75
    sample_weight_2 = 48.30

    calculator = WeightCalculator()
    difference = calculator.calculate_difference(sample_weight_1, sample_weight_2)

    print(f"The weight difference between {sample_weight_1} and {sample_weight_2} is: {difference}")