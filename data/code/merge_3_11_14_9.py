def calculate_length_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio for every pair, filtering out any pairs where the denominator is zero.
    
    Each tuple in input should be (length1, length2), resulting in length1/length2.
    
    Args:
        length_pairs (list of tuples): List where each element is a tuple (a, b).
        
    Returns:
        list: A list of floats representing the ratio a/b for valid pairs only.
              Pairs with zero denominator are excluded from the result.
              
    Raises:
        ValueError: If any pair in the input does not contain exactly two elements.
    """
    ratios = []
    
    if length_pairs is None or len(length_pairs) == 0:
        return ratios
        
    for idx, pair in enumerate(length_pairs):
        # Ensure each element is a tuple/list of at least size 2 and has no more than 2 elements
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError(f"Invalid input format at index {idx}: expected pair of length 2, got {pair}")

        try:
            numerator = float(pair[0])
            denominator = float(pair[1])
            
            # Filter out pairs where the denominator is zero or non-finite (NaN/Infinity)
            if not isinstance(denominator, (int, float)) or denominator == 0 or not finite_number(denominator):
                continue
                
            ratio = numerator / denominator
            ratios.append(ratio)
            
        except TypeError:
            # If conversion to float fails for either element, skip the pair silently 
            # unless strict error handling is required by specific use cases.
            # This ensures robustness against non-numeric inputs in pairs.
            continue
            
    return ratios

def finite_number(n):
    """Helper function to check if a number is not NaN or infinity."""
    import math
    return math.isfinite(n)

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no user input, network access, etc.)
    sample_data = [
        (10.0, 2.0),      # Normal case -> 5.0
        (4.0, 8.0),       # Ratio < 1 -> 0.5
        (-6.0, 3.0),      # Negative numerator -> -2.0
        (7.0, 0.0),       # Zero denominator: filtered out
        ([9.0], [4]),     # Invalid length pair: raises ValueError or skips based on logic above (skips here per robust design)
    ]

    try:
        result = calculate_length_ratios(sample_data)
        print("Calculated ratios:", result)
        # Expected output from valid entries only: 5.0, 0.5, -2.0
    except ValueError as e:
        print(f"Error processing input: {e}")