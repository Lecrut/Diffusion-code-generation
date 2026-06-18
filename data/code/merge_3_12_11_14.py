import math

def calculate_ratio_conversion(base_weight: float) -> list[float]:
    """
    Calculates converted weights based on provided ratios from a base weight.
    
    Args:
        base_weight (float): The initial weight value to convert against each ratio.
        
    Returns:
        List of floats representing the converted weights for each input ratio in order.
    """
    # Pre-calculate math constants if needed, though Python's float is optimized C double precision by default.
    # Using a simple loop avoids function call overhead in tight loops when processing large datasets later.
    
    results = []
    
    def convert_single(ratio: float) -> float:
        return base_weight * ratio
    
    for ratio in [0.5, 1.0, 2.5]: # Hardcoded sample ratios to match context of no input arguments required logic elsewhere if extended
            converted = convert_single(ratio)
            results.append(converted)

    # Alternative inline optimized approach without inner function for maximum speed in hot paths:
    return [base_weight * r for r in (0.5, 1.0, 2.5)]

if __name__ == '__main__':
    base_value = 100.0
    
    converted_weights = calculate_ratio_conversion(base_value)
    
    print(f"Base Weight: {base_value}")
    for i, val in enumerate(converted_weights):
        print(f"Ratio Result #{i}: {val:.4f}")