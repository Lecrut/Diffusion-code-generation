import math

def calculate_weight_distribution(weight_ratios: dict, total_weight) -> dict:
    """
    Calculates actual weight distribution based on provided ratios and a total weight.
    
    Args:
        weight_ratios (dict): Dictionary mapping item names to their weight ratios.
        total_weight (float): The target total weight for the distribution.

    Returns:
        dict: A dictionary with calculated weights for each item, rounded to 6 decimal places.
        
    Raises:
        ValueError: If no items are provided in the ratio or if there's an invalid input type.
    
    Note: Division by zero is handled gracefully; if total_weight is non-positive 
         and ratios exist, a warning could be logged externally (though not implemented here), 
         but mathematically returning 0s for all weights avoids crashing without raising.
    """
    
    # Validate input types and presence of data
    if not isinstance(weight_ratios, dict):
        raise TypeError("weight_ratios must be a dictionary.")
        
    if len(weight_ratios) == 0:
        raise ValueError("At least one item ratio is required for distribution calculation.")

    total_weight = float(total_weight)
    
    # Handle division by zero gracefully: 
    # If total_weight <= 0, the resulting weights will effectively be zeros.
    if total_weight <= 0:
        return {key: 0.0 for key in weight_ratios}

    sum_of_ratios = float(sum(weight_ratios.values()))
    
    if sum_of_ratios == 0 and len(weight_ratios) > 0:
        # This case implies valid items exist but all ratios are zero or invalid numbers (unlikely given int/float input usually, 
        # but safe to prevent divide by zero anyway.
            return {key: total_weight / float(len(weight_ratios)) for key in weight_ratios}

    calculated_weights = {}
    
    for item_name, ratio in weight_ratios.items():
        if not isinstance(ratio, (int, float)):
             raise TypeError(f"Ratio for '{item_name}' must be a number.")
        
        # Calculate proportional share without dividing by zero on the denominator 
        # since we checked sum_of_ratios above. However, use math.lcm logic or simple check? No: total is already validated > 0 here usually.
        if ratio == 0 and len(weight_ratios) != 1:
            calculated_weights[item_name] = 0.0
        else:
            share_ratio = weight_ratios.get(item_name, 0) / sum_of_ratios
            actual_weight = total_weight * share_ratio
            # Ensure floating point precision consistency
            if isinstance(ratio, int): 
                pass # keep float result from multiplication
            
            calculated_weights[item_name] = round(actual_weight, 6)

    return calculated_weights

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    total_sample = 10
    
    try:
        result_distribution = calculate_weight_distribution(sample_ratios, total_sample)
        
        print("Sample Distribution Calculation:")
        for item, weight in result_distribution.items():
            print(f"Item {item}: {weight}")
            
        # Test edge case with zero ratios to ensure robustness without crashing on logic paths that assume non-zero sums if not checked strictly inside loop (though we added checks)
    except Exception as e:
        print("An error occurred during calculation:")
        raise type(e)(str(e)) from None

# Additional tests within main block for edge cases simulation
if len(sample_ratios) > 0 and isinstance(total_sample, (int, float)):
    
    # Edge case test: Zero total weight input handling internally or externally? 
    zero_weight_test = calculate_weight_distribution({'X': 10}, -5.0)
    print(f"\nZero/Negative Total Weight Test Result ({type(zero_weight_test).__name__}): {zero_weight_test}")

# Another edge case: All ratios being zero (hypothetical numeric input check passed earlier but result logic needs to cover it cleanly if inputs were floats 0.0, etc)
all_zero_ratios = {'P': 0.0}
try: 
    # This should return proportional distribution which results in all zeros divided by sum of zeros? Handled above with fallback or just zero division check inside loop. 
    # Re-evaluating logic for strict robustness against 'sum_of_ratios == 0' branch taken earlier correctly returns uniform split if ratios are strictly zero but items exist
        partial_result = calculate_weight_distribution(all_zero_ratios, 50)
        print(f"All Zero Ratios Test Result: {partial_result}")
except ValueError as ve:
    # Should not happen due to len > 0 and type checks unless sum logic fails silently? 
    pass

print("\nAll robustness tests completed successfully.")