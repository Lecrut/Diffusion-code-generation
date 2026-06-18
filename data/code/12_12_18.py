import math

class WeightRatioConverter:
    """
    A class to handle conversion of multiple weight ratios into a normalized 
    weight distribution. It ensures that the sum of weights equals 1.0 and handles
    edge cases such as zero or negative inputs gracefully by raising appropriate exceptions.
    
    Attributes:
        None
    
    Methods:
        convert_ratios(ratios): Converts a list of non-negative ratios into normalized weights.
        
    Raises:
        ValueError: If any ratio is negative, if the sum of ratios is zero.
    """

    def __init__(self):
        self._total_ratio = 0.0
        
    def convert_ratios(self, ratios):
        """
        Converts a list of non-negative numeric weights into normalized values that 
        sum to exactly 1.0. Each input weight is multiplied by the total ratio and divided 
        by the product of all inputs (to maintain relative proportions).

        Args:
            ratios (list[float]): A list of non-negative numbers representing unnormalized weights.

        Returns:
            list[float]: Normalized weights summing to 1.0.

        Raises:
            ValueError: If any ratio is negative or if the total sum is zero.
            
        Example:
            >>> converter = WeightRatioConverter()
            >>> result = converter.convert_ratios([2, 3])
            >>> print(result)
            [0.4, 0.6]
        """
        
        # Validate input list
        if not isinstance(ratios, (list, tuple)):
            raise TypeError("Input must be a list or tuple of numbers.")

        for i, ratio in enumerate(ratios):
            if not isinstance(ratio, (int, float)) or math.isnan(ratio) or math.isinf(ratio):
                raise ValueError(f"Invalid weight at index {i}: {ratio}. Must be a finite number.")
            
            # Check for negative values and zero sum early to avoid division by zero later.
            if ratio < 0:
                raise ValueError("All weights must be non-negative.")

        total = sum(ratios)
        
        if total == 0:
            raise ValueError("The sum of all ratios is zero; normalization is impossible without at least one positive value.")
            
        # Normalize each weight by dividing it by the total. This ensures that 
        # relative proportions are preserved and they sum to exactly 1.0.
        
        normalized_weights = [ratio / total for ratio in ratios]

        return normalized_weights

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network access, or files)
    
    converter = WeightRatioConverter()
    
    # Sample 1: Simple two-item distribution
    sample_ratios_1 = [2.0, 3.0]
    normalized_distribution_1 = converter.convert_ratios(sample_ratios_1)
    print(f"Sample Input {sample_ratios_1}:")
    print(f"Normalized Distribution: {[round(w, 4) for w in normalized_distribution_1]}")

    # Sample 2: Three-item distribution with larger numbers
    sample_ratios_2 = [10.5, 20.3, 7.8]
    normalized_distribution_2 = converter.convert_ratios(sample_ratios_2)
    print(f"\nSample Input {sample_ratios_2}:")
    print(f"Normalized Distribution: {[round(w, 4) for w in normalized_distribution_2]}")

    # Sample 3: Edge case - all equal values (should result in uniform distribution)
    sample_ratios_3 = [1.0, 1.0, 1.0]
    normalized_distribution_3 = converter.convert_ratios(sample_ratios_3)
    print(f"\nSample Input {sample_ratios_3}:")
    print(f"Normalized Distribution: {[round(w, 4) for w in normalized_distribution_3]}")

    # Verify sum of first sample to demonstrate correctness (optional internal check printed here)
    total_check = round(sum(normalized_distribution_1), 6)
    assert abs(total_check - 1.0) < 1e-9, "Normalized weights must sum to exactly 1.0."
    
    print("\nAll samples processed successfully.")