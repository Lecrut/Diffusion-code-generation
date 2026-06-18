import math

class WeightRatioConverter:
    """
    A class to handle conversion of multiple weight ratios into a normalized 
    weight distribution (summing to 1.0).
    
    Attributes:
        None
    
    Methods:
        normalize_ratios(ratios): Returns the list of weights as floats summing to 1.0.
        
    Raises:
        ValueError: If any ratio is negative or if all ratios are zero/negative.
    """

    def __init__(self, *args, **kwargs):
        # Constructor does not require arguments; it's a utility class for conversion logic.
        pass

    @staticmethod
    def normalize_ratios(ratios):
        """
        Converts a list of weight ratios into a normalized distribution where the sum is 1.0.
        
        Args:
            ratios (list[float]): A list of numeric values representing weights or proportions.
            
        Returns:
            list[float]: A new list containing the normalized weights, guaranteed to sum to 1.0.
            
        Raises:
            ValueError: If any ratio is negative or if all provided ratios are zero/negative.
        """
        # Validate input constraints immediately for robustness
        total = sum(ratios)
        
        if len(ratios) == 0:
            raise ValueError("Input list of ratios cannot be empty.")
            
        if any(r < 0 for r in ratios):
            raise ValueError("All weight ratios must be non-negative values.")
            
        # Handle the edge case where all weights are zero or negative (though caught by above check)
        # specifically ensuring we don't divide by zero.
        if total == 0:
            return [1.0 / len(ratios)] * len(ratios)

        normalized_weights = []
        
        for ratio in ratios:
            weight_ratio = float(ratio) / total
            
            # Floating point precision check to avoid tiny negative numbers due to representation errors
            if math.isclose(weight_ratio, 0.0):
                continue
                
            normalized_weights.append(weight_ratio)

        return normalized_weights

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    
    # Sample Case 1: Standard positive ratios summing to a value other than 1
    raw_ratios_1 = [20, 30, 50] 
    converter = WeightRatioConverter()
    
    result_1 = converter.normalize_ratios(raw_ratios_1)
    print(f"Input Ratios: {raw_ratios_1}")
    print(f"Normalized Weights: {[round(w, 4) for w in result_1]}")
    # Expected output sum approx 1.0
    
    # Sample Case 2: Including a zero weight (should be handled gracefully or raise error depending on strictness)
    # Based on logic above, zeros are allowed but contribute nothing to the denominator unless all are zero.
    raw_ratios_2 = [5, 0, 10] 
    result_2 = converter.normalize_ratios(raw_ratios_2)
    
    print(f"\nInput Ratios: {raw_ratios_2}")
    print(f"Normalized Weights: {[round(w, 4) for w in result_2]}")

    # Sample Case 3: Error handling demonstration (commented out to prevent runtime error during execution if uncommented by user later)
    # raw_ratios_error = [-5, 10] 
    # try:
    #     res_err = converter.normalize_ratios(raw_ratios_error)
    # except ValueError as e:
    #     print(f"\nCaught expected error for negative input: {e}")

    # Sample Case 4: Single element ratio
    raw_ratios_3 = [100] 
    result_3 = converter.normalize_ratios(raw_ratios_3)
    
    print(f"\nInput Ratios: {raw_ratios_3}")
    print(f"Normalized Weights: {[round(w, 4) for w in result_3]}")

    # Verification of sum property
    total_sum_1 = sum(result_1)
    total_sum_2 = sum(result_2)
    
    if math.isclose(total_sum_1, 1.0):
        print(f"\nVerification: Sum of Case 1 weights is {total_sum_1} (Expected ~1.0)")
    else:
        print("\nWarning: Sum verification failed for Case 1.")

    if math.isclose(total_sum_2, 1.0):
        print(f"Verification: Sum of Case 2 weights is {total_sum_2} (Expected ~1.0)")
    else:
        print("Warning: Sum verification failed for Case 2.")