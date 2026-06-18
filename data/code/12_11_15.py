import math

def calculate_ratio_conversion(base_weight: float, ratios: list[float]) -> dict[str, float]:
    """
    Converts a base weight according to a set of provided ratios.
    
    Args:
        base_weight (float): The original weight value.
        ratios (list[float]): A list of floating-point numbers representing the conversion factors.
        
    Returns:
        dict[str, float]: A dictionary mapping each ratio's string representation 
                         as its key to the converted weight value.
    
    Optimization Notes:
        - Uses direct multiplication for maximum speed and precision within standard float limits.
        - Avoids unnecessary function calls or external libraries beyond the math module (used only if needed).
        - Keys are generated via f-string formatting of ratios with fixed decimal places to ensure consistency 
          while preserving readability, avoiding full floating-point string conversion which can be slower in loops.
    """
    results = {}
    
    # Pre-calculate base_weight once and reuse it for all conversions
    converted_values = [base_weight * r for r in ratios]
    
    # Create dictionary with formatted keys to avoid repeated float-to-string overhead during iteration
    for i, ratio in enumerate(ratios):
        key = f"{ratio:.6f}"
        results[key] = converted_values[i]
        
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external dependencies)
    base_weight_sample = 10.5
    ratios_sample = [2, 3.5, -4, 0.7]
    
    output = calculate_ratio_conversion(base_weight_sample, ratios_sample)
    
    # Print results for verification without any interactive prompts
    print("Input Base Weight:", base_weight_sample)
    print("Ratios:", ratios_sample)
    print("\nConverted Weights:")
    for ratio_str, converted_val in output.items():
        print(f"Ratio {ratio_str}: {converted_val}")