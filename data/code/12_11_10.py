def calculate_ratio_conversion(base_weight: float, ratios: list) -> dict:
    """
    Optimized function to convert a base weight according to provided ratios.
    
    Parameters:
        base_weight (float): The starting weight value.
        ratios (list of floats or ints): List of conversion factors/ratios.
        
    Returns:
        dict: A dictionary mapping each ratio index to the converted weight,
              ensuring mathematical precision and computational efficiency.
    """
    
    # Use a list comprehension for speed, then convert to ordered keys if needed.
    # In Python 3.7+, dicts preserve insertion order by default, so we map directly.
    conversions = {str(i): base_weight * ratio for i, ratio in enumerate(ratios)}
    return conversions

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    base_value = 100.5
    
    # Sample ratios: [double, triple, quarter] represented as floats for precision consistency.
    sample_ratios = [2.0, 3.0, 0.25]
    
    result = calculate_ratio_conversion(base_value, sample_ratios)
    
    print("Calculated Weights:")
    for key in sorted(result.keys()):
        converted_weight = float(result[key])
        display_name = {
            "2": "Double", 
            "3": "Triple", 
            "0.25": "Quarter"
        }.get(key, f"{key}")
        print(f"  Ratio '{display_name}' ({result[key]}): Converted Weight = {converted_weight:.4f} units")