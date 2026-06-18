def calculate_ratios(length_pairs):
    """
    Takes a list of tuples representing length pairs (length1, length2) 
    and returns a new list containing the ratio length1/length2.
    
    Args:
        length_pairs (list[tuple]): A list where each tuple is (length1, length2).
        
    Returns:
        list[float]: A list of ratios corresponding to valid pairs. Pairs with 
                    zero denominator are filtered out.
                    
    Raises:
        ValueError: If input contains non-tuple elements or invalid tuples.
    """
    if not isinstance(length_pairs, list):
        raise TypeError("Input must be a list.")
        
    result = []
    
    for idx, pair in enumerate(length_pairs):
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError(f"Element at index {idx} is not a valid length pair (tuple of two numbers).")
            
        try:
            length1 = float(pair[0])
            length2 = float(pair[1])
        except (ValueError, TypeError):
            continue  # Skip pairs where conversion fails
            
        if length2 == 0:
            continue  # Filter out zero denominators
        
        result.append(length1 / length2)
        
    return result

if __name__ == '__main__':
    sample_data = [
        (4, 8),
        (6, 3),
        (10, 5),
        (7, 0),      # Will be filtered out due to zero denominator
        (9.5, 2.3),
        ("invalid", "data"),  # Will skip during conversion
    ]
    
    ratios = calculate_ratios(sample_data)
    print(f"Calculated ratios: {ratios}")