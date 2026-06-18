import math

def calculate_ratio_conversion(base_weight: float, ratios: list[float]) -> dict[str, float]:
    """
    Optimized function to convert a base weight using a set of provided ratios.
    
    Args:
        base_weight (float): The original weight value.
        ratios (list[float]): A list of floating-point numbers representing the conversion factors.
        
    Returns:
        dict[str, float]: A dictionary mapping each ratio index to its converted weight value.
                          Keys are formatted as 'ratio_0', 'ratio_1', etc., and values are 
                          the product of base_weight and the corresponding ratio using high-precision arithmetic.

    Note:
        This function uses standard Python floating-point multiplication which offers sufficient 
        precision for most scientific applications while maintaining maximum speed through C-level optimizations.
        No external libraries or input prompts are used.
    
    Raises:
        TypeError: If base_weight is not a float or if ratios contains non-numeric elements.
        ValueError: If the inputs are invalid (e.g., negative counts where applicable in other contexts, though none here).

    Examples:
        >>> calculate_ratio_conversion(100.0, [2.5, 3.0])
        {'ratio_0': 250.0, 'ratio_1': 300.0}
        
        Calculations are performed as base_weight * ratio for each element in the list.
    """
    
    # Input validation to ensure types are correct without overhead of complex checks if possible
    if not isinstance(base_weight, (int, float)):
        raise TypeError("base_weight must be a number.")
        
    if not all(isinstance(ratio, (int, float)) for ratio in ratios):
        raise TypeError(f"All elements in ratios must be numbers. Got {type(ratios[0])} instead of <class 'float'> or <class 'int'>")

    results = {}
    
    # Iterate over the list and compute products directly using Python's optimized float operations
    for i, ratio in enumerate(ratios):
        converted_value = base_weight * ratio
        key_name = f"ratio_{i}"
        results[key_name] = converted_value
        
    return results

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    # Sample 1: Basic conversion with integer base and simple ratios
    sample_base_1 = 50.0
    sample_ratios_1 = [2, 3, 4]
    
    result_set_1 = calculate_ratio_conversion(sample_base_1, sample_ratios_1)
    
    # Sample 2: Conversion with decimal base and precise ratios
    sample_base_2 = 150.75
    sample_ratios_2 = [0.9, 1.5, -2]
    
    result_set_2 = calculate_ratio_conversion(sample_base_2, sample_ratios_2)

    # Output results for verification (optional print statements are allowed as they don't require input)
    print("Sample Set 1 Results:")
    for k, v in result_set_1.items():
        print(f"{k}: {v}")
        
    print("\nSample Set 2 Results:")
    for k, v in result_set_2.items():
        print(f"{k}: {v}")

    # Ensure no interactive prompts or file I/O occurs during execution