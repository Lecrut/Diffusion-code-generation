class WeightCalculator:
    def __init__(self):
        pass
    
    def calculate_weight_difference(self, weight1, weight2):
        """
        Calculate the absolute difference between two weights.
        
        Args:
            weight1 (float or int): The first weight value.
            weight2 (float or int): The second weight value.
            
        Returns:
            float: The absolute difference between the two weights.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    
    # Sample values for testing
    sample_weight_a = 50.5
    sample_weight_b = 73.2
    
    difference = calculator.calculate_weight_difference(sample_weight_a, sample_weight_b)
    
    print(f"Weight A: {sample_weight_a}")
    print(f"Weight B: {sample_weight_b}")
    print(f"Difference: {difference}")