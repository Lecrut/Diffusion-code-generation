def calculate_length_ratios(length_pairs):
    """
    Calculates the ratio (length1 / length2) for each tuple in the input list,
    excluding any pair where length2 is zero.

    Args:
        length_pairs (list of tuples): A list containing pairs of integers or floats.
                                      Each element should be a tuple (length1, length2).

    Returns:
        list: A new list of ratios corresponding to the input pairs with non-zero denominators.
              If no valid ratios can be calculated, returns an empty list.
    
    Raises:
        TypeError: If any element in the input is not a tuple or if it's not exactly two elements long.
    """
    results = []
    
    for pair in length_pairs:
        # Validate that each item is a tuple/list of exactly 2 items
        try:
            l1, l2 = list(pair)
            
            # Ensure we have the correct number of dimensions (though unpacking handles loose types if fixed len logic isn't needed elsewhere)
            # The prompt implies strict tuples but robustness for lists as pairs is often preferred unless specified otherwise.
            # However, to strictly follow "tuple", let's ensure it works for list too just in case input varies slightly on form while keeping type safety.
            
            if len(pair) != 2:
                raise ValueError(f"Expected a pair of two values, got {len(pair)} elements")
                
        except TypeError as e:
            # This catches cases where 'pair' is not iterable or doesn't support indexing properly in this context
            raise TypeError("All items must be pairs (e.g., tuples/lists with 2 elements). Input contains invalid format.") from None

        if l2 == 0:
            continue
            
        ratio = l1 / l2
        results.append(ratio)
    
    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access needed.
    sample_data = [
        (4, 8),      # Ratio: 0.5
        (10, 2),     # Ratio: 5.0
        (7, 3),      # Ratio: ~2.33
        (9, 0),      # Skipped due to zero denominator
        (-6, -4),    # Ratio: 1.5
        (5 * float('inf'), 2) # Float infinity handling works in standard division
    ]

    result_ratios = calculate_length_ratios(sample_data)
    
    print("Input Pairs:", sample_data)
    print("Calculated Ratios:", [f"{r:.4g}" if isinstance(r, (float)) else r for r in result_ratios])