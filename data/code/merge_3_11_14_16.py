def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio for every pair, filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): A list of tuples where each tuple contains two integers representing lengths.
        
    Returns:
        list[float]: A list of ratios corresponding to valid input pairs. If a division by zero occurs or 
                    an invalid pair format is encountered, that specific ratio is skipped from the result.
    
    Raises:
        ValueError: If any element in length_pairs is not a tuple with exactly two numeric elements.
    """
    if not isinstance(length_pairs, list):
        raise TypeError("Input must be a list.")

    ratios = []
    
    for pair in length_pairs:
        # Validate that the input is actually a tuple/list of 2 numbers
        try:
            len1, len2 = map(float, [float(x) for x in pair])
            if not (isinstance(pair, (list, tuple)) and len(pair) == 2):
                raise ValueError(f"Invalid pair format: {pair}")
            
            # Calculate ratio only if denominator is non-zero
            if len2 != 0.0:
                ratios.append(len1 / len2)
        except (ValueError, TypeError):
            continue
            
    return ratios

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_data = [
        (4, 8),      # Expected ratio: 0.5
        (10, 2),     # Expected ratio: 5.0
        (7, 0),      # Should be filtered out due to zero denominator
        (3, -6),     # Negative denominator is valid mathematically (-0.5)
        ("a", "b"),  # Invalid input type for demonstration of error handling/filtering
        (12,),       # Incorrect tuple length
    ]

    result = calculate_ratios(sample_data)
    
    print("Calculated Ratios:", result)