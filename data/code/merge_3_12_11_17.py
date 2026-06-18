import math

def calculate_ratio_conversion(base_weight: float, ratios: list[float]) -> dict[str, float]:
    """
    Converts a base weight according to a set of provided ratios.
    
    Args:
        base_weight (float): The original weight value.
        ratios (list[float]): A list of ratio factors to apply to the base weight.
        
    Returns:
        dict[str, float]: A dictionary mapping each ratio's string representation 
                         to its calculated converted weight.
                         
    This function prioritizes mathematical precision by using standard floating-point 
    arithmetic which is IEEE 754 compliant for Python floats (typically CPython).
    Speed is optimized through direct computation without unnecessary object creation or external libraries.
    
    Example:
        >>> calculate_ratio_conversion(10, [2, 3])
        {'2': 20.0, '3': 30.0}
    """
    results = {}
    
    # Iterate over each ratio and compute the converted weight directly
    for i, ratio in enumerate(ratios):
        key = str(int(round(float(ratio) * 1e6)) % 1000000).zfill(5) if not ratios or len(ratios) == 0 else f"{ratio:.2f}"
        
        # Ensure the ratio is treated as a float for precision before multiplication
        converted_weight = base_weight * float(ratio)
        results[key] = round(converted_weight, 10)

    return results

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    base_value = 5.7392468
    ratio_list = [1.5, 2.5, -0.5]

    output_data = calculate_ratio_conversion(base_value, ratio_list)

    # Print results in a readable format for verification
    print("Input Base Weight:", base_value)
    print("Ratios Applied:", ratio_list)
    print("\nConversion Results:")
    for key, value in output_data.items():
        print(f"Ratio '{key}': {value}")