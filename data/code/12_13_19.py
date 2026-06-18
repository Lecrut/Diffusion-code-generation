def calculate_weight_distribution(weight_ratios: dict, total_weight: float) -> dict:
    """
    Calculates actual weights based on a ratio dictionary and a total weight.
    
    Handles potential division by zero gracefully by returning None if the 
    sum of ratios is 0 (though this would imply an invalid input state).

    Args:
        weight_ratios (dict): A dictionary mapping item identifiers to their relative weights.
                               Example: {'A': 2, 'B': 3}
        total_weight (float): The desired final total sum of all calculated weights.

    Returns:
        dict or None: A new dictionary with actual weights for each key in input.
                      If the sum of ratios is zero and a result is attempted to be computed 
                      without knowing which items are present, returns None to indicate invalid scaling factor.
    
    Raises:
        ValueError: If total_weight is negative (though this could also imply an impossible physical state).
    """
    if not isinstance(weight_ratios, dict):
        raise TypeError("weight_ratios must be a dictionary")

    # Calculate the sum of all ratio parts to determine the scaling factor.
    try:
        total_ratio = sum(weight_ratios.values())
    except Exception as e:
        return None  # Graceful handling for unexpected errors in summation
    
    if total_weight < 0:
        raise ValueError("Total weight cannot be negative.")

    if total_ratio == 0.0 and len(weight_ratios) > 0:
        # All ratios are zero, or the sum is effectively zero due to precision issues with zeros.
        return None
    
    scale_factor = total_weight / total_ratio

    distribution = {}
    
    for item in weight_ratios.keys():
        try:
            calculated_value = round(weight_ratios[item] * scale_factor)
            # Note: Using int or float? The prompt implies physical weights, so floats are safer 
            # but often rounded to reasonable precision. However, exact arithmetic is requested implicitly.
            distribution[item] = weight_ratios[item] * scale_factor
        except Exception as e:
            return None

    return distribution

if __name__ == '__main__':
    sample_weight_ratio = {'A': 2, 'B': 3}
    total_sample_weight = 10.5
    
    result_distribution = calculate_weight_distribution(sample_weight_ratio, total_sample_weight)
    
    if result_distribution is not None:
        print("Calculated Distribution:")
        for item, weight in result_distribution.items():
            print(f"Item {item}: {weight}")
        
        # Verify sum matches input (within float precision tolerance)
        calculated_total = sum(result_distribution.values())
        assert abs(calculated_total - total_sample_weight) < 1e-6, "Sum mismatch detected."
    else:
        print("Error in calculation logic.")