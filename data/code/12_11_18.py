import math

def calculate_ratio_conversion(base_weight: float, ratios: list) -> list:
    """
    Calculates converted weights based on provided ratio factors relative to a base weight.

    This function prioritizes mathematical precision by using the `float` type (IEEE 754 double-precision),
    which offers greater accuracy than integers for large or fractional values, while maintaining 
    performance comparable to integer arithmetic due to native hardware support in modern CPUs.
    
    Args:
        base_weight (float): The starting weight value.
        ratios (list[float]): A list of numerical factors representing the conversion ratio.

    Returns:
        list[float]: A list containing the calculated converted weights corresponding to each input ratio.
    """
    return [base_weight * r for r in ratios]

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, network access, or file dependencies are required.
    
    base_value = 100.5
    
    # Define a list of weight conversion factors (ratios)
    ratio_set = [2.0, 3/4, -0.5, 16] 
    
    result_weights = calculate_ratio_conversion(base_value, ratio_set)
    
    print(f"Base Weight: {base_value}")
    print("Ratios and Converted Weights:")
    for i, (ratio, converted) in enumerate(zip(ratio_set, result_weights), start=1):
        print(f"{i}. Ratio ({ratio}): {converted:.6f}")