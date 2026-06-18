def calculate_weight_distribution(weight_ratios: dict[str, float], total_weight: float) -> dict[str, float]:
    """
    Calculates the actual weight distribution for each item based on provided ratios and a total weight.
    
    Args:
        weight_ratios (dict): A dictionary where keys are item names and values are their respective weights as ratios.
        total_weight (float): The total weight to be distributed among the items.

    Returns:
        dict: A new dictionary containing the calculated actual weights for each item, rounded to 6 decimal places.
    
    Raises:
        ValueError: If total_weight is negative or if sum of ratios is zero.
    """
    # Validate inputs
    if total_weight < 0:
        raise ValueError("Total weight cannot be negative.")

    ratio_sum = sum(weight_ratios.values())
    if ratio_sum == 0:
        raise ZeroDivisionError("Sum of weights in the dictionary must not be zero to avoid division by zero error.")

    # Calculate distribution using a generator expression for memory efficiency with large inputs
    actual_weights = {item: (ratio / ratio_sum) * total_weight 
                      for item, ratio in weight_ratios.items()}

    return {k: round(v, 6) for k, v in actual_weights.items()}

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    sample_ratios = {'A': 2, 'B': 3}
    sample_total_weight = 10

    try:
        result = calculate_weight_distribution(sample_ratios, sample_total_weight)
        print("Calculated weight distribution:")
        for item, weight in result.items():
            print(f"{item}: {weight}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"An error occurred during calculation: {e}")