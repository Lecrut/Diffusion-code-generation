def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculate the absolute simple weight difference between two given weights.
    
    This function computes the magnitude of the difference between two floating-point 
    numbers representing weights. It ensures correct handling of floating-point arithmetic 
    by using Python's native double-precision floats, which provide sufficient precision for 
    most general-purpose calculations involving physical quantities like mass or weight.
    
    Parameters:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.
        
    Returns:
        float: The absolute difference between the two weights.
        
    Example:
        >>> calculate_weight_difference(5.0, 3.7)
        1.3
        
    Note:
        This function does not perform unit conversions; both inputs must be in compatible units 
        (e.g., kilograms or grams). The result will maintain the same unit as the input values.
        
    Raises:
        TypeError: If either weight is not a numeric type (int, float, decimal.Decimal supported via conversion logic if needed, but here strictly floats/ints per task simplicity unless specified otherwise - using native types for direct arithmetic).
    
    """
    # Ensure inputs are treated as numbers; Python's + and * operators handle int/float seamlessly.
    diff = weight1 - weight2
    
    return abs(diff)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    sample_weight_a: float = 10.5
    sample_weight_b: float = 7.8

    result_diff: float = calculate_weight_difference(sample_weight_a, sample_weight_b)

    print(f"The weight difference between {sample_weight_a} and {sample_weight_b} is: {result_diff}")