def calculate_weight_distribution(weight_ratios: dict, total_weight: float) -> dict:
    """
    Calculates the actual weight distribution based on provided ratios and a total weight.
    
    Args:
        weight_ratios (dict): A dictionary where keys are item identifiers and values 
                              represent their respective weights in proportion to others.
        total_weight (float): The desired sum of all calculated weights.
        
    Returns:
        dict: A new dictionary containing the actual weights for each item.
              If division by zero occurs due to invalid input, returns an empty dict.
    
    Raises:
        ValueError: If weight_ratios is not a non-empty dictionary or total_weight is negative.
    """
    if not isinstance(weight_ratios, dict) or len(weight_ratios) == 0:
        raise ValueError("weight_ratios must be a non-empty dictionary.")
    if total_weight < 0:
        raise ValueError("total_weight cannot be negative.")

    # Calculate the sum of all ratios to determine the scaling factor.
    ratio_sum = sum(weight_ratios.values())
    
    # Handle potential division by zero gracefully as per task requirements.
    if ratio_sum == 0:
        return {}

    distribution = {}
    for item, ratio in weight_ratios.items():
        calculated_weight = (ratio / ratio_sum) * total_weight
        distribution[item] = round(calculated_weight, 6) # Round to avoid floating point noise issues
    
    return distribution

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    
    # Sample Case 1: Simple ratio calculation
    ratios_sample_1 = {'A': 2, 'B': 3}
    total_weight_1 = 50
    
    result_1 = calculate_weight_distribution(ratios_sample_1, total_weight_1)
    print(f"Sample 1 Result (Total: {total_weight_1}):")
    for item, weight in result_1.items():
        print(f"{item}: {weight}")

    # Sample Case 2: More complex ratios with larger numbers
    ratios_sample_2 = {'X': 5, 'Y': 7, 'Z': 3}
    total_weight_2 = 100
    
    result_2 = calculate_weight_distribution(ratios_sample_2, total_weight_2)
    print(f"\nSample 2 Result (Total: {total_weight_2}):")
    for item, weight in result_2.items():
        print(f"{item}: {weight}")

    # Sample Case 3: Edge case where ratio sum is zero (handled gracefully by returning empty dict)
    ratios_sample_3 = {'P': 0} 
    total_weight_3 = 10
    
    try:
        result_3 = calculate_weight_distribution(ratios_sample_3, total_weight_3)
        print(f"\nSample 3 Result (Zero Ratio Sum):")
        if not result_3:
            print("No valid weights calculated due to zero ratio sum.")
        else:
            for item, weight in result_3.items():
                print(f"{item}: {weight}")
    except ValueError as e:
        # This specific case (zero value) is handled inside the function logic 
        # but if we wanted strict enforcement of non-zero values before calculation, it would raise here.
        # Based on "handle gracefully", returning empty dict is preferred over raising for zero sum ratios.
        pass

    print("\nAll samples executed successfully without external input.")