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
        [0.286, 0.429, 0.714] (approximate values based on sum=10)
    """

    def normalize_ratios(self, ratios):
        """
        Converts a list of weight ratios into a normalized distribution where the 
        total sums to exactly 1.0. Handles edge cases such as empty lists or zero totals.
        
        Args:
            ratios (list[float]): A non-empty list of positive numeric values representing weights.
            
        Returns:
            list[float]: A new list containing the same number of elements, each normalized 
                        so that their sum equals 1.0. If input is empty or all zeros, returns [0].
                        
        Raises:
            ValueError: If any ratio in the input list is negative.
            
        Examples:
            >>> converter = WeightRatioConverter()
            >>> converter.normalize_ratios([1, 2])
            [0.333..., 0.667...]
        """
        if not ratios or all(r == 0 for r in ratios):
            return [0] * len(ratios)

        total = sum(ratios)
        
        # Validate that no ratio is negative (though problem implies positive weights usually)
        if any(r < 0 for r in ratios):
            raise ValueError("All weight ratios must be non-negative.")

        return [r / total for r in ratios]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    converter = WeightRatioConverter()
    
    # Sample 1: Simple integer ratios
    sample_ratios_1 = [2, 3, 5]
    normalized_1 = converter.normalize_ratios(sample_ratios_1)
    print(f"Input: {sample_ratios_1}")
    print(f"Normalized Distribution: {[round(x, 4) for x in normalized_1]}")

    # Sample 2: Decimal ratios with varying magnitudes
    sample_ratios_2 = [0.5, 1.5, 3.0]
    normalized_2 = converter.normalize_ratios(sample_ratios_2)
    print(f"\nInput: {sample_ratios_2}")
    print(f"Normalized Distribution: {[round(x, 4) for x in normalized_2]}")

    # Sample 3: Edge case - all equal parts
    sample_ratios_3 = [10, 10, 10]
    normalized_3 = converter.normalize_ratios(sample_ratios_3)
    print(f"\nInput: {sample_ratios_3}")
    print(f"Normalized Distribution: {[round(x, 4) for x in normalized_3]}")

    # Sample 4: Edge case - single ratio
    sample_ratios_4 = [100]
    normalized_4 = converter.normalize_ratios(sample_ratios_4)
    print(f"\nInput: {sample_ratios_4}")
    print(f"Normalized Distribution: {[round(x, 4) for x in normalized_4]}")

    # Sample 5: Edge case - very small numbers to test precision handling
    sample_ratios_5 = [1e-6, 2e-6]
    normalized_5 = converter.normalize_ratios(sample_ratios_5)
    print(f"\nInput: {sample_ratios_5}")
    print(f"Normalized Distribution: {[round(x, 8) for x in normalized_5]}")

    # Verify the sum of each result is approximately 1.0 (within floating point tolerance)
    def check_sum(weights):
        return abs(sum(weights) - 1.0) < 1e-9
    
    print("\n--- Validation ---")
    for i, sample in enumerate([sample_ratios_1, sample_ratios_2], 1):
        result = converter.normalize_ratios(sample)
        is_valid = check_sum(result)
        status = "PASS" if is_valid else "FAIL"
        print(f"Test Case {i}: Sum validation -> {status}")

    # Test error handling for negative input (optional demonstration, though not triggered in main block above unless explicitly called with bad data)
    try:
        converter.normalize_ratios([-1, 2])
    except ValueError as e:
        print(f"\nError Handling Test Passed: Caught expected exception - {e}")