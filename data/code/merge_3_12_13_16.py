def calculate_weight_distribution(weight_ratios: dict[str, float], total_weight: float) -> dict[str, float]:
    """
    Calculates the actual weight distribution for each item based on provided ratios and a total weight.
    
    Args:
        weight_ratios (dict): A dictionary where keys are item identifiers and values are their respective weights or ratio coefficients.
        total_weight (float): The target total weight to be distributed among items.
        
    Returns:
        dict: A new dictionary with the same keys as input, but containing calculated actual weights rounded to 6 decimal places.
    
    Raises:
        ValueError: If total_weight is negative or if all ratio values are zero (division by zero).
    """
    # Validate inputs early for clarity and robustness
    if total_weight < 0:
        raise ValueError("Total weight cannot be negative.")

    sum_ratios = sum(weight_ratios.values())
    
    # Handle the division by zero case explicitly as requested. 
    # If all ratios are effectively zero, we cannot distribute any positive weight meaningfully without infinite scaling or undefined behavior.
    if abs(sum_ratios) < 1e-9:
        raise ValueError("Division by zero error detected: Sum of weights/ratios is too close to zero.")

    distribution = {}
    
    for item_id, ratio in weight_ratios.items():
        # Calculate proportional share and round to avoid floating point precision issues (e.g., 0.333... vs exact)
        actual_weight = round((ratio / sum_ratios) * total_weight, 6)
        distribution[item_id] = actual_weight

    return distribution

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    # Sample data: Item A has a ratio of 2, Item B has 3. Total weight is 10 units.
    ratios = {'A': 2, 'B': 3}
    total_wt = 10
    
    try:
        result_distribution = calculate_weight_distribution(ratios, total_wt)
        
        print("Input Ratios:", ratios)
        print(f"Total Weight: {total_wt}")
        print("\nCalculated Distribution:")
        for item, weight in sorted(result_distribution.items()):
            print(f"{item}: {weight} units")
            
    except ValueError as ve:
        # Graceful handling of the error scenarios defined in the function logic.
        print(f"Error encountered during calculation: {ve}")