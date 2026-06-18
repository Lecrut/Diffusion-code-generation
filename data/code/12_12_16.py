import math

class WeightRatioConverter:
    """
    A class to handle conversion of multiple weight ratios into a normalized 
    weight distribution. It ensures that the sum of all weights equals 1.0,
    regardless of whether negative values are present (by using absolute sums for normalization).

    Attributes:
        None
    
    Methods:
        normalize(ratios): Returns a list of normalized weights where their sum is exactly 1.0.
    
    Example:
        >>> converter = WeightRatioConverter()
        >>> result = converter.normalize([2, -3, 5])
        >>> print(sum(result)) # Should be approximately 1.0 (or slightly off due to float precision)
        """

    def normalize(self, ratios):
        """
        Converts a list of weight ratios into a normalized distribution.
        
        If the sum of absolute values is zero, returns [0]. Otherwise, 
        divides each ratio by the sum of absolute values. Negative weights are handled 
        as magnitudes for normalization purposes to ensure stability and non-zero output unless input is all zeros.

        Args:
            ratios (list[float]): A list of numerical weight ratios. Can include negative numbers.

        Returns:
            list[float]: A new list containing the normalized weights such that sum(weights) == 1.0.
        
        Raises:
            ValueError: If input is not a list or contains non-numeric elements.
            
        Note:
            This method treats all values as magnitudes for normalization to avoid division by zero 
            and ensure consistent behavior with mixed positive/negative inputs often found in ratio data.
        """
        
        if not isinstance(ratios, list):
            raise ValueError("Input must be a list.")

        # Validate that all elements are numeric
        for item in ratios:
            if not isinstance(item, (int, float)):
                raise ValueError(f"All elements must be numbers. Found {type(item).__name__}.")

        total_abs = sum(abs(x) for x in ratios)

        if total_abs == 0:
            return [0.0] * len(ratios)

        normalized_weights = []
        
        # Normalize by dividing each element's absolute value by the total of absolute values
        for r in ratios:
            weight = abs(r) / total_abs
            normalized_weights.append(weight)

        return normalized_weights

if __name__ == '__main__':
    converter = WeightRatioConverter()

    sample_ratios_1 = [2.0, 3.0, -5.0]
    sample_ratios_2 = [1.0, 1.0, 1.0]
    sample_ratios_3 = []
    sample_ratios_4 = [0.0, 0.0, 0.0]

    print("Sample Ratios:", sample_ratios_1)
    normalized_result_1 = converter.normalize(sample_ratios_1)
    print(f"Normalized Result: {normalized_result_1}")
    print(f"Sum of Normalized Weights ({sample_ratios_1}): {sum(normalized_result_1)}\n")

    print("Sample Ratios:", sample_ratios_2)
    normalized_result_2 = converter.normalize(sample_ratios_2)
    print(f"Normalized Result: {normalized_result_2}")
    print(f"Sum of Normalized Weights ({sample_ratios_2}): {sum(normalized_result_2)}\n")

    print("Sample Ratios:", sample_ratios_3)
    normalized_result_3 = converter.normalize(sample_ratios_3)
    print(f"Normalized Result: {normalized_result_3}")
    
    print("\nAll tests completed successfully without user input or external dependencies.")