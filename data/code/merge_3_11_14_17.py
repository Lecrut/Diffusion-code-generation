def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio for every pair, filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): A list of tuples, each containing two integers representing lengths.
        
    Returns:
        list[float]: A list of ratios corresponding to valid input pairs.
    """
    result = []
    for pair in length_pairs:
        if len(pair) != 2 or not isinstance(pair[0], (int, float)) or not isinstance(pair[1], (int, float)):
            continue
        
        numerator = pair[0]
        denominator = pair[1]
        
        if denominator == 0:
            continue
            
        ratio = numerator / denominator
        result.append(ratio)
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access needed)
    sample_data = [
        (10, 5),
        (20, 4),
        (30, 0),   # Should be filtered out due to zero denominator
        (7, 8),
        (100, -20), # Negative denominator is allowed unless specified otherwise; here we allow it as per general math rules. 
                    # If strictly positive denominators were needed, an extra check could be added.
    ]

    ratios = calculate_ratios(sample_data)
    
    print("Input pairs:", sample_data)
    print("Calculated ratios (zero denominator filtered):", ratios)