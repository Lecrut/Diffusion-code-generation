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
        >>> result = converter.normalize_ratios([2, 3])
        >>> print(result)
        [0.4, 0.6]
    """

    def normalize_ratios(self, ratios):
        """
        Converts a list of weight ratios into a normalized distribution where the sum is exactly 1.0.
        
        Args:
            ratios (list[float]): A non-empty list of positive numbers representing relative weights.
            
        Returns:
            list[float]: The same number of elements as input, scaled so that their sum equals 1.0.
            
        Raises:
            ValueError: If the input list is empty or contains any non-positive values.
        """
        if not ratios:
            raise ValueError("Input ratio list cannot be empty.")

        for r in ratios:
            if r <= 0:
                raise ValueError("All weight ratios must be positive numbers.")

        total = sum(ratios)
        
        # Normalize by dividing each ratio by the total sum
        normalized_weights = [r / total for r in ratios]
        
        return normalized_weights

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    converter = WeightRatioConverter()

    # Sample Case 1: Simple two-part ratio (e.g., parts of a mixture)
    sample_ratios_1 = [2, 3]
    
    # Sample Case 2: Three-component distribution with larger numbers
    sample_ratios_2 = [0.5, 1.0, 4.0]

    # Sample Case 3: Integers representing relative importance scores
    sample_ratios_3 = [10, 20, 30, 40]

    print("Sample Ratios:", sample_ratios_1)
    normalized_result_1 = converter.normalize_ratios(sample_ratios_1)
    print(f"Normalized Weights (Case 1): {normalized_result_1}")
    
    # Verify sum is approximately 1.0 with floating point tolerance
    assert abs(sum(normalized_result_1) - 1.0) < 1e-9, "Sum of weights should be 1.0"

    print("\nSample Ratios:", sample_ratios_2)
    normalized_result_2 = converter.normalize_ratios(sample_ratios_2)
    print(f"Normalized Weights (Case 2): {normalized_result_2}")

    assert abs(sum(normalized_result_2) - 1.0) < 1e-9, "Sum of weights should be 1.0"

    print("\nSample Ratios:", sample_ratios_3)
    normalized_result_3 = converter.normalize_ratios(sample_ratios_3)
    print(f"Normalized Weights (Case 3): {normalized_result_3}")

    assert abs(sum(normalized_result_3) - 1.0) < 1e-9, "Sum of weights should be 1.0"

    # Demonstrate error handling with a non-positive value
    try:
        converter.normalize_ratios([5, -2])
    except ValueError as e:
        print(f"\nError caught for invalid input: {e}")

    # Demonstrate error handling with empty list
    try:
        converter.normalize_ratios([])
    except ValueError as e:
        print(f"Error caught for empty input: {e}")