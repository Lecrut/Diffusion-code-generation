def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the calculated ratio (length1 / length2) for every pair, filtering out 
    any pairs where the denominator is zero.
    
    Args:
        length_pairs: List of tuples, each tuple contains two numbers representing lengths
        
    Returns:
        List of ratios as floats, excluding cases where division by zero would occur
    """
    ratios = []
    for pair in length_pairs:
        length1, length2 = pair[0], pair[1]
        if length2 != 0:
            ratio = length1 / length2
            ratios.append(ratio)
    
    return ratios

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [
        (4, 8),
        (6, 3),
        (10, 2),
        (5, 0),      # Should be filtered out due to zero denominator
        (7, 14),
        (-3, -9),    # Negative numbers are valid in this context
        (2.5, 5.0)   # Floats should also work correctly
    ]

    result = calculate_ratios(sample_data)
    
    print("Input Pairs:")
    for pair in sample_data:
        print(f"({pair[0]}, {pair[1]})")
        
    print("\nCalculated Ratios (excluding zero denominators):")
    for i, ratio in enumerate(result):
        original_input = sample_data[i] if result else None
        expected_ratio = original_input[0] / original_input[1] if any(original_input) and original_input[1] != 0 else "N/A"
        print(f"{original_input} -> {ratio:.2f}")

    # Verify that the zero denominator case was correctly filtered out (should be index 4 in result, but skipped)
    assert len(result) == 6, "Should have exactly 6 ratios after filtering"
    expected_ratio_zero_case = sample_data[0][0] / sample_data[0][1]
    actual_first_ratio = result[0] if result else None
    
    print(f"\nVerification passed. Total valid ratios: {len(result)}")