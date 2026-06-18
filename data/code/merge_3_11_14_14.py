def calculate_length_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list 
    containing the calculated ratio for every pair, filtering out 
    any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): List of tuples, each tuple contains two numbers representing lengths.
        
    Returns:
        list[float]: A list of ratios corresponding to valid input pairs.
                     Ratios are calculated as first_length / second_length.
                     Pairs with a zero denominator are excluded from the result.
    
    Raises:
        ValueError: If any element in length_pairs is not a tuple or if it contains non-numeric values.
    """
    ratios = []
    
    for pair in length_pairs:
        # Validate input structure and types
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError(f"Each element must be a tuple of exactly two numbers. Got {pair}.")
        
        try:
            length1 = float(pair[0])
            length2 = float(pair[1])
            
            # Filter out pairs where the denominator is zero
            if length2 == 0:
                continue
                
            ratio = length1 / length2
            ratios.append(ratio)
            
        except (TypeError, ValueError):
            raise ValueError(f"Invalid numeric values in pair {pair}.")

    return ratios

if __name__ == '__main__':
    # Hard-coded sample values for testing
    sample_data = [
        (10.5, 2),
        (4, 8),
        (7, 0),      # Will be filtered out due to zero denominator
        (3.5, -6),   # Negative denominator is allowed as long as it's not zero
        ("invalid", 5), # Invalid type for demonstration of error handling logic if uncommented in a broader context
    ]

    try:
        result = calculate_length_ratios(sample_data)
        print("Calculated ratios:", result)
        
        # Additional verification to ensure filtering worked correctly
        assert len(result) == 3, "Expected 3 valid ratios (excluding the zero denominator case)."
        expected_ratio_1 = 5.25   # 10.5 / 2
        expected_ratio_2 = 0.5    # 4 / 8
        expected_ratio_3 = -0.5833333333333334 # 3.5 / -6
        
        assert abs(result[0] - expected_ratio_1) < 1e-9, "First ratio mismatch."
        assert abs(result[1] - expected_ratio_2) < 1e-9, "Second ratio mismatch."
        
    except ValueError as e:
        print(f"Error occurred during calculation: {e}")