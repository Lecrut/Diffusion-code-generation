def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio for every pair, filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs: List of tuples, each tuple contains two integers representing lengths.
        
    Returns:
        A list of floats or None values representing the ratios (length1 / length2). 
        If a division by zero would occur, returns None for that pair instead.
        
    Raises:
        ValueError: If any element in the input is not an integer.
    """
    
    result = []
    
    if not isinstance(length_pairs, list):
        raise TypeError("Input must be a list.")
        
    for i, (length1, length2) in enumerate(length_pairs):
        # Check if elements are integers to ensure valid input type
        try:
            int_length1 = int(length1)
            int_length2 = int(length2)
            
            # If denominator is zero, skip this pair by appending None or a specific indicator. 
            # The problem asks to filter out pairs where denominator is zero from the result list?
            # Re-reading: "returns a new list containing the calculated ratio for every pair, filtering out any pairs"
            # This implies removal of those pairs entirely if possible, but usually in such tasks 
            # it means returning None or raising an error. Given standard practices and safety, 
            # we will return None to represent that specific pair was filtered/skipped due to zero denominator.
            
            if int_length2 == 0:
                result.append(None)
                
        except (ValueError, TypeError):
            raise ValueError(f"Invalid input at index {i}: Elements must be integers.")

    # However, a common interpretation of "filtering out" in list processing contexts 
    # when dealing with invalid data points is to exclude them entirely. 
    # Let's re-evaluate: If I have [ (10, 5), (20, 0) ], should the output be [2.0] or [2.0, None]?
    # The prompt says "filtering out any pairs where the denominator is zero". This usually means exclusion.
    # But if we exclude them completely from the result list corresponding to their index position? 
    # Or just return a new list of valid ratios and drop invalid ones?
    # Let's assume the latter (drop invalid entries) as it creates a clean list of successful calculations.
    
    final_ratios = []
    for length1, length2 in length_pairs:
        try:
            int_length1 = int(length1)
            int_length2 = int(length2)
            
            if int_length2 == 0:
                continue # Skip this pair
            
            ratio = float(int_length1 / int_length2)
            final_ratios.append(ratio)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid input encountered.")

    return final_ratios

if __name__ == '__main__':
    sample_data = [
        (4, 8),   # Ratio: 0.5
        (10, 2),  # Ratio: 5.0
        (3, 6),   # Ratio: 0.5
        (7, 0),   # Denominator is zero -> Filter out / Skip
        (9, 3)    # Ratio: 3.0
    ]

    output = calculate_ratios(sample_data)
    
    print("Input pairs:", sample_data)
    print("Calculated ratios:")
    for i, ratio in enumerate(output):
        if ratio is None:
            print(f"Pair {i}: Skipped (division by zero)")
        else:
            print(f"Pair {i}: {ratio}")