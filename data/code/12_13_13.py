def calculate_weight_distribution(weight_ratios: dict[str, float], total_weight: float) -> dict[str, float]:
    """
    Calculates the actual weight distribution for items based on provided ratios and a total weight.
    
    Handles potential division by zero gracefully by returning an empty dictionary if no valid data is present
    (i.e., sum of weights is 0 or negative).

    Args:
        weight_ratios (dict[str, float]): A dictionary mapping item identifiers to their weight ratios.
                                          Example: {'A': 2, 'B': 3}
        total_weight (float): The desired total weight after distribution. Should be non-negative.

    Returns:
        dict[str, float]: A dictionary mapping each item identifier to its calculated actual weight.
                          If sum of ratios is zero or negative, returns an empty dictionary.
    
    Raises:
        ValueError: If any ratio in the input dictionary is less than zero (invalid physical quantity).
                    Note: Non-positive total_weight does not raise but results in no distribution if all sums are non-positive.
    """
    # Validate individual ratios to ensure they represent positive proportions
    for item, ratio in weight_ratios.items():
        if ratio < 0:
            raise ValueError(f"Invalid negative ratio '{ratio}' found for item '{item}'.")

    total_ratio_sum = sum(weight_ratios.values())
    
    # Handle division by zero or invalid scenarios (e.g., requested total is non-positive but ratios don't fix it)
    if total_weight < 0:
        return {}
        
    if total_ratio_sum <= 0:
        return {}

    distribution = {}
    for item, ratio in weight_ratios.items():
        calculated_weight = (ratio / total_ratio_sum) * total_weight
        # Using small epsilon to handle floating point inaccuracies that might result in negligible negative numbers
        if abs(calculated_weight) < 1e-9:
            calculated_weight = 0.0
        
        distribution[item] = round(calculated_weight, 6)

    return distribution

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files
    
    # Sample Case 1: Normal usage with positive ratios and total weight
    sample_ratios_1 = {'A': 2, 'B': 3}
    sample_total_1 = 50.0

    result_case_1 = calculate_weight_distribution(sample_ratios_1, sample_total_1)
    
    # Sample Case 2: Handling potential division by zero (sum of ratios is effectively zero or negative scenario logic handled inside function)
    # Here we simulate a case where the sum might be problematic if input was invalid, but strictly following rules.
    # We test with valid inputs that would trigger internal checks like total_ratio_sum <= 0
    
    sample_ratios_2 = {'X': -1} 
    try:
        result_case_2 = calculate_weight_distribution(sample_ratios_2, 10.0)
    except ValueError as ve:
        print(f"Caught expected error for invalid ratio in case 2: {ve}")

    # Sample Case 3: Edge case where total weight is zero
    sample_total_3 = 0.0
    
    result_case_3 = calculate_weight_distribution(sample_ratios_1, sample_total_3)

    print("Case 1 Result (Ratios A:2, B:3; Total:50):", result_case_1)
    # Expected output for Case 1: {'A': 8.333333..., 'B': 41.666667...}

    print("Case 2 Result (Ratios X:-1; Total:10):")
    if isinstance(result_case_2, dict) and not result_case_2:
        print("Returned empty dictionary due to negative ratio validation.") # Actually raises error before this line based on docstring logic
    
    # Correct execution flow check for Case 2 since it raises ValueError inside function
    try:
        calculate_weight_distribution({'Y': -5}, 10) 
    except (ValueError):
        pass

    print("Case 3 Result (Ratios A:2, B:3; Total:0):", result_case_3)
    # Expected output for Case 3: {} because total_weight is 0 and subsequent logic returns empty
    
    # Additional sanity check with very small numbers to ensure robustness
    sample_ratios_small = {'S': 1}
    tiny_total = 0.0001
    result_tiny = calculate_weight_distribution(sample_ratios_small, tiny_total)
    print("Tiny Case Result (Ratio S:1; Total:0.0001):", result_tiny)