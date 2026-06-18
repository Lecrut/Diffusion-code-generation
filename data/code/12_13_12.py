def calculate_weight_distribution(weight_ratios: dict[str, float], total_weight: float) -> dict[str, float]:
    """
    Calculates the actual weight distribution based on provided ratios and a total weight.
    
    Args:
        weight_ratios (dict): A dictionary where keys are item identifiers (strings) 
                             and values represent their relative weights as floats or integers.
        total_weight (float): The target total weight to be distributed among items.

    Returns:
        dict[str, float]: A new dictionary containing the calculated actual weights for each item.

    Raises:
        ValueError: If total_weight is negative or if sum of ratios is zero.
    
    Note: This function does not handle division by zero gracefully in terms of suppressing 
            errors; instead, it raises a clear exception to prevent silent failures when 
            the input data is invalid (i.e., all ratios are zero).
    """
    total_ratio = 0
    
    # Validate that no ratio is negative and calculate sum of ratios
    for item, ratio in weight_ratios.items():
        if ratio < 0:
            raise ValueError(f"Negative ratio found for item '{item}'. Ratios must be non-negative.")
        
        total_ratio += float(ratio)

    # Handle division by zero case explicitly as per robustness requirement
    if total_ratio == 0:
        raise ZeroDivisionError("Sum of weight ratios is zero. Cannot distribute weights without valid proportions.")

    distribution = {}
    
    for item, ratio in weight_ratios.items():
        calculated_weight = (ratio / total_ratio) * total_weight
        # Round to a reasonable precision to avoid floating point artifacts like 0.9999999999999998
        distribution[item] = round(calculated_weight, 6)

    return distribution

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    
    # Sample dictionary of weight ratios and total weight
    sample_ratios: dict[str, float] = {'A': 2, 'B': 3}
    sample_total_weight: float = 10.5

    try:
        result_distribution = calculate_weight_distribution(sample_ratios, sample_total_weight)
        
        print("Calculated Weight Distribution:")
        for item, weight in result_distribution.items():
            print(f"{item}: {weight}")
            
    except ZeroDivisionError as e:
        # Graceful handling of the specific division by zero scenario raised internally
        error_message = f"Calculation failed due to invalid input ratios. Error details: {e}"
        print(error_message)
        
    except ValueError as e:
        # Handle negative ratio errors gracefully
        error_message = f"Invalid data detected. Error details: {e}"
        print(error_message)