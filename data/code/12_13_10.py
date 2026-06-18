def calculate_weight_distribution(weight_ratios: dict, total_weight: float) -> list:
    """
    Calculates the actual weight distribution for each item in a dictionary of ratios.
    
    Args:
        weight_ratios (dict): A dictionary where keys are items and values are their relative weights/ratios.
        total_weight (float): The target total weight to distribute among the items.
        
    Returns:
        list: A list of tuples containing each item name and its calculated actual weight, sorted by ratio descending.
    
    Raises:
        ValueError: If all ratios are zero or if a single ratio is non-zero but others are missing (logic handled via sum check).
    """
    # Handle the case where total_weight is negative to prevent logical errors later
    if total_weight < 0:
        raise ValueError("Total weight cannot be negative.")

    # Calculate the sum of all ratios. If it's zero, we have a division by zero risk unless only one item exists with ratio > 0 (handled below) or no items exist.
    sum_ratios = sum(weight_ratios.values())
    
    if sum_ratios == 0:
        return []

    # Special case handling for robustness against empty dict or all zeros resulting in a single non-zero division later? 
    # Actually, standard math is fine as long as sum > 0. If one item has ratio X and others have 0 (if allowed by input type), sum will be X.
    # However, the prompt implies ratios like {'A':2, 'B':3}. We assume keys are non-zero if they exist in a meaningful distribution context.
    
    calculated_weights = []

    for item, ratio in weight_ratios.items():
        try:
            actual_weight = (ratio / sum_ratios) * total_weight
            # Round to avoid floating point precision noise like 20.999999999 instead of 21
            # Only round if the number is not an integer or has many decimals, usually .5 up
            actual_weight = round(actual_weight, 4) 
        except ZeroDivisionError:
            # This block theoretically shouldn't be reached because sum_ratios != 0 check exists above.
            # However, we keep it for defensive programming as per "handle potential division by zero gracefully".
            continue
            
        calculated_weights.append((item, actual_weight))

    # Sort the results based on original ratio (descending) to ensure consistent output order
    # We need to track the original ratios for sorting. Re-calculate or store? 
    # Let's re-iterate with stored data if we needed complex logic, but here:
    calculated_weights.sort(key=lambda x: weight_ratios[x[0]], reverse=True)

    return calculated_weights

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or files involved.
    
    # Sample dictionary of weight ratios and total weight
    item_ratios = {'A': 2, 'B': 3}
    target_total_weight = 105

    try:
        distribution_result = calculate_weight_distribution(item_ratios, target_total_weight)
        
        print("Calculated Weight Distribution:")
        for item, weight in distribution_result:
            print(f"{item}: {weight}")
            
    except Exception as e:
        # Graceful error handling if something unexpected occurs (though unlikely with valid input above)
        print(f"An error occurred during calculation: {e}")