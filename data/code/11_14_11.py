def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list 
    containing the calculated ratio (length1 / length2) for every pair,
    filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): List of tuples with two integers each.
        
    Returns:
        list[float]: List of ratios corresponding to valid input pairs.
    """
    result_ratios = []
    for pair in length_pairs:
        if len(pair) != 2 or not isinstance(pair, tuple):
            continue
        numerator, denominator = pair
        
        # Check if the second value (denominator) is zero and handle it by skipping
        # Note: Using '0' to be safe against float inputs that might be effectively zero
        if denominator == 0:
            continue
            
        ratio = numerator / denominator
        result_ratios.append(ratio)
    
    return result_ratios

if __name__ == '__main__':
    sample_data = [
        (10, 2),      # Expected: 5.0
        (7, 3),       # Expected: ~2.333...
        (4, 0),       # Skipped due to zero denominator
        (-8, -4),     # Expected: 2.0
        (100, 5)      # Expected: 20.0
    ]

    calculated_results = calculate_ratios(sample_data)
    
    print("Input pairs and their corresponding ratios:")
    for i, pair in enumerate(sample_data):
        numerator, denominator = pair
        if denominator == 0:
            status = "SKIPPED (division by zero)"
        else:
            ratio_val = calculated_results[i] if i < len(calculated_results) else None
            status = f"Ratio: {ratio_val}"
        
        print(f"{pair} -> {status}")

    # Print the final list of valid ratios
    print("\nFinal List of Ratios:", calculated_ratios_list := calculate_ratios(sample_data))