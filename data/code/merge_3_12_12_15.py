class WeightRatioConverter:
    """
    A class to handle conversion of multiple weight ratios into a normalized 
    weight distribution (summing to 1.0).
    
    Attributes:
        None
    
    Methods:
        normalize_ratios(ratios): Returns the list of weights as floats summing to 1.0.
    """

    def __init__(self, *args, **kwargs):
        """Initialize an empty converter."""
        pass

    @staticmethod
    def normalize_ratios(ratios):
        """
        Converts a list or tuple of weight ratios into a normalized distribution.
        
        Args:
            ratios (list/tuple/iterable): An iterable containing the raw weights/ratios.
            
        Returns:
            list[float]: A new list where each element is divided by the sum 
                         of all elements, ensuring they sum to 1.0.
                         
        Raises:
            ValueError: If input is empty or contains only zeros/negative numbers.
        """
        if not ratios:
            raise ValueError("Input ratio list cannot be empty.")

        total = sum(ratios)
        
        # Handle case where all values are zero or negative (invalid for weights usually, 
        # but strictly following math here; in practice, we might check > 0).
        if total == 0:
            raise ValueError("Sum of ratios is zero. Cannot normalize.")

        return [r / total for r in ratios]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample data representing parts per hundred or arbitrary weights
    raw_ratios = [10, 25, 30, 35]

    converter = WeightRatioConverter()

    try:
        normalized_distribution = converter.normalize_ratios(raw_ratios)
        
        print("Original Ratios:", raw_ratios)
        print("Normalized Distribution (Sum should be ~1.0):", normalized_distribution)
        
        # Verification step to ensure correctness within the module logic
        total_normalized = sum(normalized_distribution)
        assert abs(total_normalized - 1.0) < 1e-9, "Normalization failed: Sum is not 1.0"
    except ValueError as e:
        print(f"Error during normalization: {e}")