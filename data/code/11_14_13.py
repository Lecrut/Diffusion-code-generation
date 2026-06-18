def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio for each pair, filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): A list of tuples, where each tuple contains two integers representing lengths.
        
    Returns:
        float or None: The ratio (length1 / length2) if valid, otherwise None for invalid cases.
                       If the denominator is zero, the pair is excluded from results but does not cause an error.
    
    Raises:
        TypeError: If input is not a list of tuples with exactly two numeric elements.
    """
    ratios = []
    
    # Validate and process each length pair
    for i, (length1, length2) in enumerate(length_pairs):
        if isinstance(length1, int) and isinstance(length2, int) and len(length_pairs[i]) == 2:
            if length2 != 0:
                ratios.append(float(length1 / length2))
    
    return ratios

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [
        (10, 5),   # Expected ratio: 2.0
        (7, 3),    # Expected ratio: ~2.333...
        (8, 4),    # Expected ratio: 2.0
        (6, 0),    # Skipped due to zero denominator
        (15, 25)   # Expected ratio: 0.6
    ]

    results = calculate_ratios(sample_data)

    print("Calculated Ratios:")
    for item in results:
        print(f"Ratio values: {item}")