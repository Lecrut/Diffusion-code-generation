def calculate_weight_distribution(weight_ratios: dict[str, int], total_weight: float) -> dict[str, float]:
    """
    Calculates the actual weight distribution based on provided ratios and a total weight.

    Args:
        weight_ratios (dict): A dictionary where keys are item identifiers and values represent relative weights.
                              Example: {'A': 2, 'B': 3}
        total_weight (float): The total absolute weight to be distributed among the items.

    Returns:
        dict: A new dictionary containing each key from input with its calculated actual weight as a float.

    Raises:
        ValueError: If total_weight is non-positive or if sum of ratios is zero.
    
    Note: This function does not raise errors for division by zero because it validates the condition beforehand,
                  ensuring robustness while avoiding runtime exceptions in valid scenarios. The error handling 
                  covers invalid inputs that would cause mathematical impossibilities (zero ratio sum).

    Example usage: calculate_weight_distribution({'A': 2, 'B': 3}, 10) returns {'A': 4.0, 'B': 6.0}
    """
    
    # Validate total weight to ensure it's positive for meaningful distribution
    if not isinstance(total_weight, (int, float)) or total_weight <= 0:
        raise ValueError("Total weight must be a positive number.")

    # Calculate the sum of all ratio values
    total_ratio = sum(weight_ratios.values())

    # Handle division by zero case where all ratios are zero
    if total_ratio == 0:
        return {key: 0.0 for key in weight_ratios}

    # Compute each item's actual weight using the formula: (ratio / total_rations) * total_weight
    result = {}
    for key, ratio in weight_ratios.items():
        calculated_value = (ratio / total_ratio) * total_weight
        result[key] = float(calculated_value)

    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    # Sample 1: Basic distribution with positive integers and standard total weight.
    sample_data_1 = {
        'item_a': {'ratios': {'A': 2, 'B': 3}, 'total_weight': 50}
    }

    result_sample_1 = calculate_weight_distribution({'A': 2, 'B': 3}, 50)
    
    # Sample 2: Edge case where total weight is zero (handled gracefully by returning zeros).
    sample_data_2 = {
        'item_b': {'ratios': {'X': 1, 'Y': 1}, 'total_weight': 0}
    }

    result_sample_2 = calculate_weight_distribution({'X': 1, 'Y': 1}, 0)
    
    # Sample 3: Division by zero scenario in terms of ratios (all zeros).
    sample_data_3 = {
        'item_c': {'ratios': {'P': 0, 'Q': 0}, 'total_weight': 25}
    }

    result_sample_3 = calculate_weight_distribution({'P': 0, 'Q': 0}, 25)

    # Output results directly to console for verification. No user interaction required.
    print("Sample Result (Total Weight: 50):")
    print(result_sample_1)

    print("\nEdge Case - Zero Total Weight:")
    print(result_sample_2)

    print("\nEdge Case - All Ratios Are Zero:")
    print(result_sample_3)