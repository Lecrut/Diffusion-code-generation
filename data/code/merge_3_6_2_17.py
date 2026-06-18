class WeightCalculator:
    """A class to perform basic weight calculations."""

    def calculate_difference(self, weight1, weight2):
        """Calculate the difference between two weights.
        
        Args:
            weight1 (float or int): The first weight value.
            weight2 (float or int): The second weight value.
            
        Returns:
            float: The absolute difference between the two weights.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Sample values for testing without user input
    sample_weight_1 = 80.5
    sample_weight_2 = 75.0

    calculator = WeightCalculator()
    result = calculator.calculate_difference(sample_weight_1, sample_weight_2)

    print(f"Difference between {sample_weight_1} and {sample_weight_2}: {result}")