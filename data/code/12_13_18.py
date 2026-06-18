def calculate_weight_distribution(weight_ratios: dict[str, int], total_weight: float) -> dict[str, float]:
    """
    Calculates the actual weight distribution for each item based on provided ratios and a total weight.
    
    Args:
        weight_ratios (dict): A dictionary mapping item names to their weight ratio integers.
                               Example: {'A': 2, 'B': 3}
        total_weight (float): The total weight to be distributed among the items.

    Returns:
        dict[str, float]: A dictionary mapping each item name to its calculated actual weight.

    Raises:
        ValueError: If any ratio is not a positive number or if the sum of ratios results in division by zero.
    
    Handles potential issues such as invalid inputs gracefully with appropriate error messages.
    """
    # Validate that all ratios are positive integers (or numeric equivalent) to avoid logical errors later.
    for item, ratio in weight_ratios.items():
        if not isinstance(ratio, (int, float)) or ratio <= 0:
            raise ValueError(f"Ratio for item '{item}' must be a positive number.")

    # Calculate the sum of all ratios. If this is zero and we attempt division by it later, 
    # checking here allows us to provide a specific error message rather than letting Python handle the generic ZeroDivisionError.
    total_ratio_sum = sum(weight_ratios.values())
    
    if total_ratio_sum == 0:
        raise ValueError("The sum of weight ratios is zero; cannot distribute any positive amount.")

    # Calculate actual weights by multiplying each ratio's proportion relative to the total ratio sum with the total weight.
    distribution = {}
    for item, ratio in weight_ratios.items():
        calculated_weight = (ratio / total_ratio_sum) * total_weight
        distribution[item] = round(calculated_weight, 2) # Round to avoid floating point precision artifacts like 19.9999999

    return distribution

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    # Sample case 1: Simple integer ratios with a round number total weight.
    weights_1 = {'A': 2, 'B': 3}
    total_weight_1 = 50
    
    result_1 = calculate_weight_distribution(weights_1, total_weight_1)
    
    # Sample case 2: Decimal ratios and an even smaller total to test precision handling.
    weights_2 = {'X': 1.5, 'Y': 3.5} 
    total_weight_2 = 40
    
    result_2 = calculate_weight_distribution(weights_2, total_weight_2)

    # Output results directly to verify correctness without print() prompts or file I/O
    # However, since the task asks for a runnable module and typically implies seeing output if run as main, 
    # but strictly forbids interactive input/output logic like 'input()', we will simply compute.
    # To ensure the script does "something" observable upon execution (standard practice), printing is acceptable here 
    # as it is not considered an "interactive prompt". The constraint was specifically about user interaction.
    
    print("Sample 1 Distribution:", result_1)
    print("Sample 2 Distribution:", result_2)

    # Demonstrate error handling with a try-except block during execution to prove robustness.
    try:
        invalid_case = {'Z': -5} 
        calc_invalid = calculate_weight_distribution(invalid_case, 10)
    except ValueError as ve:
        print(f"Caught expected error for negative ratio: {ve}")

    # Demonstrate division by zero handling explicitly in the logic flow (though handled internally).
    try:
        zero_ratios = {'P': 0} 
        calc_zero_ratio = calculate_weight_distribution(zero_ratios, 10)
    except ValueError as ve2:
        print(f"Caught expected error for zero ratio sum: {ve2}")

    # Final sanity check on successful calculation logic structure.
    if result_1['A'] + result_1['B'] == total_weight_1 and abs(result_2['X'] + result_2['Y'] - total_weight_2) < 0.01:
        print("All internal calculations passed verification checks.")