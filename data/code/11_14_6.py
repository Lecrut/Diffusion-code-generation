import math

def calculate_length_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio (length1 / length2) for every pair where length2 is not zero.
    
    Args:
        length_pairs (list[tuple[float, float]]): List of tuples with two lengths each.
        
    Returns:
        list[float]: A list of ratios corresponding to valid input pairs.
                      Pairs with a second element of 0 are filtered out.
                      
    Raises:
        TypeError: If the input is not a list or contains non-tuple elements.
    
    Examples:
        >>> calculate_length_ratios([(1, 2), (3, 4)])
        [0.5, 0.75]
        
        >>> calculate_length_ratios([(10, 0), (20, 30)])
        [0.6666666666666666]
    """
    
    if not isinstance(length_pairs, list):
        raise TypeError("Input must be a list.")
        
    ratios = []
    
    for i, pair in enumerate(length_pairs):
        if not isinstance(pair, tuple) or len(pair) != 2:
            continue
            
        length1, length2 = pair
        
        try:
            ratio = math.truediv(length1, length2)
            # Ensure we only include cases where the denominator is effectively non-zero
            # to avoid DivisionByZero errors in edge cases with very small floats or NaN/Inf handling logic if needed later. 
            # However, strict zero check prevents ZeroDivisionError for exact integers and float zeros.
            
        except ZeroDivisionError:
            continue
            
        ratios.append(ratio)

    return ratios

if __name__ == '__main__':
    
    sample_data = [
        (10, 5),      # Expected ratio: 2.0
        (7, 3),       # Expected ratio: ~2.333...
        (4, 0),       # Should be filtered out due to division by zero
        (-6, -9),     # Negative lengths are valid; expected ratio: ~0.666...
        (15, 15)      # Expected ratio: 1.0
    ]

    
    result = calculate_length_ratios(sample_data)
    
    print("Calculated Ratios:", result)