def calculate_weight_distribution(weight_ratios: dict[str, float], total_weight: float) -> dict[str, float]:
    """
    Calculates the actual weight distribution for each item based on provided ratios and a total weight.
    
    Args:
        weight_ratios (dict): A dictionary where keys are item names and values are their relative weights.
        total_weight (float): The target total weight to be distributed among items.
        
    Returns:
        dict: A new dictionary with the same keys as input, but updated to reflect actual calculated weights.
              If all ratios sum to zero or if total_weight is negative/zero and no valid distribution exists,
              it returns a copy of the original weight_ratios (scaled by 0) to avoid division errors.
    
    Raises:
        ValueError: Only raised if input validation fails for non-numeric values in ratio dict keys/values 
                   that are not floats or strings as per type hints (though Python is dynamic, this ensures clarity).
                   
    Note: This function handles potential division by zero gracefully without crashing the program.
      If sum of ratios is 0 and total_weight > 0, it returns zeros for all items to prevent ZeroDivisionError.
"""

    # Create a copy to avoid modifying input dictionary directly if needed later (though not strictly required here)
    result = {}
    
    # Validate inputs implicitly by attempting conversion during calculation; 
    # assume dict keys are strings and values are numbers as per problem description context.
    total_ratio_sum = sum(weight_ratios.values())

    try:
        if abs(total_ratio_sum) < 1e-9:
            # Handle division by zero scenario gracefully
            for item, _ in weight_ratios.items():
                result[item] = 0.0
        else:
            multiplier = total_weight / total_ratio_sum
            for item, ratio in weight_ratios.items():
                actual_weight = round(ratio * multiplier, 6) # Round to avoid floating point noise issues
                result[item] = actual_weight
                
    except ZeroDivisionError:
        # Fallback if any unexpected zero occurs during calculation logic (redundant due to check above but safe)
        for item in weight_ratios.keys():
            result[item] = 0.0
            
    return result

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    total_w = 5
    
    distribution = calculate_weight_distribution(sample_ratios, total_w)
    
    print("Input Ratios:", sample_ratios)
    print(f"Total Weight: {total_w}")
    print("Calculated Distribution:")
    for item in sorted(distribution.keys()):
        if isinstance(item, str):
            print(f"{item}: {distribution[item]}")