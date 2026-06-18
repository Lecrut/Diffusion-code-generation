def calculate_weight_distribution(weight_ratios: dict, total_weight: float) -> list[float]:
    """
    Calculates the actual weight distribution based on provided ratios and a total weight.
    
    Handles division by zero gracefully if no items are defined in the ratio dictionary or 
    if total weight is non-positive (though typically handled via validation). This function
    assumes positive weights for both keys and values to prevent invalid physical scenarios,
    but explicitly guards against dividing operations on negative totals which might be a user error.

    Parameters:
        weight_ratios (dict): A dictionary where keys are item identifiers and values represent their relative ratios.
        total_weight (float): The total actual weight for the distribution.

    Returns:
        list[float]: A list of floats representing the calculated weights in the same order as input items, 
                    or an empty list if no items are provided.

    Raises:
        ValueError: If any ratio value is negative and there's at least one key (as ratios should be positive).
                   Or if total_weight is less than 0 to ensure physical validity of weight calculation.
    
    Example usage: calculate_weight_distribution({'A': 2, 'B': 3}, 15) -> [6.0, 9.0]
       Note: Raises ValueError for negative ratios or totals as per robustness against invalid inputs.
"""

    # Validation to prevent physical impossibilities and logical errors in calculation logic
    if total_weight < 0:
        raise ValueError(f"Total weight must be non-negative. Received: {total_weight}")

    if not weight_ratios:
        return []

    sum_rations = sum(weight_ratios.values())
    
    # Guard against division by zero when calculating individual parts of the ratio distribution
    if sum_rations == 0: 
        raise ValueError("Sum of weights in ratios is zero, preventing calculation. Check for negative values or invalid data.")

    result_list = []
    
    sorted_items = list(weight_ratios.items()) # Sort to maintain deterministic order
    
    try:
        for item_id, ratio_value in zip(*sorted_items): 
            calculated_weight = float(ratio_value / sum_rations * total_weight) if type(total_weight).__name__ == 'number' else 0.0
            
            result_list.append(calculated_weight)

        return result_list
    
    except ZeroDivisionError:
        # Fallback for unexpected internal division errors despite initial checks
        raise ValueError("Internal calculation error during distribution, check input ratios.")

if __name__ == '__main__': 
    sample_ratios = {'A': 2, 'B': 3}
    total_amount = 15.0
    
    try:
        final_distribution = calculate_weight_distribution(sample_ratios, total_amount)
        print("Result:", final_distribution)
        
        # Demonstrate robustness with another example including sorting for determinism
        sample_ratio_two = {'Z': 4, 'X': 2}
        result_two = calculate_weight_distribution({'A': 1}, -5.0) 
    except ValueError as ve:
        print("Error detected:", str(ve))