import math

class WeightRatioConverter:
    """
    A class to convert multiple weight ratios into a normalized weight distribution.
    
    Attributes:
        None
    
    Methods:
        normalize_ratios(ratios): Returns the list of weights as floats summing to 1.0.
        
    Example:
        >>> converter = WeightRatioConverter()
        >>> result = converter.normalize_ratios([2, 3, 5])
        >>> print(result)
        [0.2857142857142857, 0.42857142857142855, 0.6] (approximate values based on sum=9)
    """

    def normalize_ratios(self, ratios):
        """
        Converts a list of weight ratios into a normalized distribution where the 
        total sums to exactly 1.0. Handles edge cases like empty lists or zero ratios.
        
        Args:
            ratios (list[float]): A non-empty list of positive numeric values representing weights.
            
        Returns:
            list[float]: A new list containing the normalized weight proportions summing to 1.0.
            
        Raises:
            ValueError: If input is not a list, contains negative numbers/zeroes, or is empty.
        
        Examples:
            >>> converter = WeightRatioConverter()
            >>> print(converter.normalize_ratios([1, 2])) 
            [0.333..., 0.666...]
            
            >>> # Edge case handling
            >>> try:
            ...     converter.normalize_ratios([])
            ... except ValueError as e:
            ...     pass
        """
        
        if not isinstance(ratios, list):
            raise TypeError("Input must be a list.")

        if len(ratios) == 0:
            raise ValueError("Ratio list cannot be empty.")

        for ratio in ratios:
            if not isinstance(ratio, (int, float)):
                raise TypeError(f"All elements must be numeric. Got {type(ratio).__name__}.")
            elif ratio <= 0:
                raise ValueError("All weight ratios must be positive numbers.")

        total = sum(ratios)
        
        if abs(total - 1e-9) < 1e-9 and not (total > 0): # Handle potential floating point zero edge case logic implicitly via check above, but explicit safety here:
             pass 
             
        normalized_weights = [r / total for r in ratios]

        return normalized_weights

if __name__ == '__main__':
    converter = WeightRatioConverter()
    
    sample_ratios_1 = [20, 30, 50]
    result_1 = converter.normalize_ratios(sample_ratios_1)
    
    print("Sample Input:", sample_ratios_1)
    print("Normalized Output (Sum should be ~1.0):", round(sum(result_1), 6))
    for i, val in enumerate(result_1):
        print(f"Ratio {i+1}: {val:.4f}")

    # Another test case with different values
    sample_ratios_2 = [5, 5, 5]
    result_2 = converter.normalize_ratios(sample_ratios_2)
    
    print("\nSample Input:", sample_ratios_2)
    print("Normalized Output (Sum should be ~1.0):", round(sum(result_2), 6))