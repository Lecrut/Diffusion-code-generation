def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio for every pair, filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): A list of tuples where each tuple contains two numbers.
        
    Returns:
        list[float]: A list of ratios corresponding to non-zero denominators in the input.
                     If a pair has a zero as the second element, it is skipped from results.
    
    Example:
        [[(10, 2), (5, 0), (8, 4)], -> [5.0]
    """
    ratios = []
    for length_pair in length_pairs:
        if len(length_pair) != 2 or any(not isinstance(x, (int, float)) for x in length_pair):
            continue
        
        numerator, denominator = length_pair[0], length_pair[1]
        
        if denominator == 0:
            continue
            
        ratios.append(numerator / denominator)
    
    return ratios

if __name__ == '__main__':
    sample_data = [
        (10, 2),
        (5, 0),      # Denominator is zero; will be filtered out
        (8, 4),
        (-3.5, 7),   # Negative numerator allowed
        (0, 9)       # Zero numerator allowed
    ]

    result = calculate_ratios(sample_data)
    
    print("Input pairs:", sample_data)
    print("Calculated ratios (excluding zero denominators):", result)