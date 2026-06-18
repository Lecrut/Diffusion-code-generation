def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the ratio for every pair, filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): A list of tuples, each tuple contains two integers representing lengths.
        
    Returns:
        list[float]: A list of ratios calculated as first element divided by second element from input pairs.
                     Pairs with a zero denominator are excluded.
    """
    result = []
    
    for length1, length2 in length_pairs:
        if length2 != 0:
            ratio = length1 / length2
            result.append(ratio)
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or network access needed)
    sample_data = [
        (10, 5),   # Expected ratio: 2.0
        (8, 4),    # Expected ratio: 2.0
        (7, 3),    # Expected ratio: ~2.333...
        (6, 0),    # Skipped due to zero denominator
        (5, 1),    # Expected ratio: 5.0
        (9, -3)    # Expected ratio: -3.0
    ]

    calculated_ratios = calculate_ratios(sample_data)

    print("Input Pairs:", sample_data)
    print("Calculated Ratios:", calculated_ratios)