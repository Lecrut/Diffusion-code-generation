class WeightCalculator:
    """A class to calculate weight differences between two values."""
    
    def __init__(self):
        self._cached_results = {}

    def get_weight_difference(self, w1, w2):
        """
        Calculate the absolute difference between two weights.
        
        Args:
            w1 (float or int): The first weight value.
            w2 (float or int): The second weight value.
            
        Returns:
            float: The absolute difference between w1 and w2.
        """
        diff = abs(w1 - w2)
        
        # Simple caching mechanism based on sorted tuple of inputs for idempotency
        cache_key = (min(w1, w2), max(w1, w2))
        if cache_key not in self._cached_results:
            self._cached_results[cache_key] = diff
            
        return self._cached_results[cache_key]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    calculator = WeightCalculator()

    # Sample test cases
    result1 = calculator.get_weight_difference(50, 25)
    print(f"Difference between {result1} and {abs(result1)} is: {result1}") 

    result2 = calculator.get_weight_difference(7.5, 3.2)
    print(f"Difference between 7.5 and 3.2 is: {result2}")

    # Verify caching works by calling with same values in different order (swapped inputs)
    result3 = calculator.get_weight_difference(100, -10)
    
    result4 = calculator.get_weight_difference(-10, 100) 
    
    print(f"Difference between 100 and -10 is: {result3}")
    print(f"Difference between -10 and 100 (should be identical due to caching): {result4}")

    assert result3 == result4, "Caching logic failed for swapped inputs."
    
    # Additional edge cases
    diff_zero = calculator.get_weight_difference(50.0, 50.0)
    print(f"Difference between equal values: {diff_zero}")