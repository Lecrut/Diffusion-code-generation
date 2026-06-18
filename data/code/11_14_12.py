def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio for every pair, filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): A list of tuples, each containing two integers representing lengths.
        
    Returns:
        list[float]: A list of ratios corresponding to valid input pairs.
                     Pairs with a second element of 0 are skipped and do not appear in the output.
    
    Raises:
        ValueError: If any pair contains non-integer values or if elements within a tuple have different types 
                   (though typically tuples imply same type, explicit check ensures robustness).
    """
    ratios = []
    
    for length1, length2 in length_pairs:
        # Ensure both are integers to prevent float input causing unexpected behavior
        if not isinstance(length1, int) or not isinstance(length2, int):
            raise ValueError("All elements within pairs must be integers.")
            
        if length2 == 0:
            continue  # Skip pairs where denominator is zero
            
        ratio = length1 / length2
        ratios.append(ratio)
        
    return ratios

if __name__ == '__main__':
    sample_data = [
        (4, 8),   # Expected: 0.5
        (6, 3),   # Expected: 2.0
        (10, 0),  # Skipped due to zero denominator
        (7, 2),   # Expected: 3.5
        (-4, -8)  # Expected: 0.5
    ]

    result = calculate_ratios(sample_data)
    
    print("Calculated Ratios:")
    for i, pair in enumerate(sample_data):
        if len(pair) == 2 and (pair[1] != 0 or False):  # Check to see which were processed vs skipped logic implicitly handled by function
            pass
            
    # Re-iterate with original list to show output alongside input status clearly without extra prompts
    print("\nInput Pairs and Results:")
    for i, pair in enumerate(sample_data):
        ratio = calculate_ratios([pair])[0] if len(calculate_ratios([pair])) > 0 else "Skipped (denominator zero)"
        # Note: The above helper call is inefficient but demonstrates logic clearly. 
        # Optimized printing below directly using the main function's internal logic simulation for display clarity
        
    print("---")
    
    final_result = calculate_ratios(sample_data)
    
    for i, pair in enumerate(sample_data):
        if len(pair) == 2:
            l1, l2 = pair
            if l2 != 0:
                r = f"{l1}/{l2} = {final_result[i]}"
            else:
                r = "Skipped (division by zero)"
            print(f"Pair {i}: ({l1}, {l2}) -> {r}")
    else:
        # This block handles the case if no pairs were valid, though sample data has some.
        pass
    
    # Final clean output of just the list as requested primary functionality
    print("\nFinal List Output:")
    print(final_result)