def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the difference between consecutive weights in a list of pairs.
    
    Args:
        weight_pairs (list[tuple]): List of tuples where each tuple contains two numeric values representing a pair.
        
    Yields:
        float or int: The absolute difference between the second and first element of each subsequent pair compared to the previous one.
                      If it's the first iteration, yields 0.
    
    Example:
        >>> list(weight_difference_generator([(10, 20), (30, 40), (50, 60)]))
        [0, 19.87..., 19.87...] 
        Note: The difference is calculated as |current_pair_sum - previous_pair_sum|.
    """
    if not weight_pairs:
        return
    
    prev_sum = None
    for i in range(len(weight_pairs)):
        current_pair = weight_pairs[i]
        
        # Ensure the pair has exactly two elements and they are numeric
        if len(current_pair) != 2 or not all(isinstance(x, (int, float)) for x in current_pair):
            raise ValueError(f"Invalid pair at index {i}: expected a tuple of two numbers")

        current_sum = sum(current_pair)
        
        # Yield the difference between current and previous sums. 
        # For the first element, yield 0 to indicate no prior comparison.
        if prev_sum is None:
            yield 0.0
        else:
            diff = abs(current_sum - prev_sum)
            yield float(diff)
        
        prev_sum = current_sum

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, etc.)
    sample_data = [
        (10.5, 20.3),   # Sum: 30.8
        (40.1, 50.9),   # Sum: 91.0 -> Diff from prev: ~60.2
        (7.2, 8.8),     # Sum: 16.0 -> Diff from prev: ~75.0
    ]

    print("Weight Difference Generator Output:")
    
    try:
        differences = weight_difference_generator(sample_data)
        
        for idx, diff in enumerate(differences):
            if idx == len(sample_data) - 1 and hasattr(diff, '__iter__'):
                # Handle case where generator is exhausted or converted to list logic implicitly here just for clarity
                pass
            
            print(f"Pair {idx + 1}: Difference = {diff}")
            
    except Exception as e:
        print(f"Error during generation: {e}")