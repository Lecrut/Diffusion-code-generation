def compare_length_lists(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine maximums, minimums, and the overall range difference.

    Args:
        list_a (list[float]): First list of lengths.
        list_b (list[float]): Second list of lengths.

    Returns:
        dict[str, float]: A dictionary containing 'max_combined', 'min_combined', 
                         and 'range_difference'.
    """
    
    # Combine both lists to find the global maximum and minimum values across all inputs
    combined_list = []
    
    for length in list_a:
        if isinstance(length, (int, float)):
            combined_list.append(float(length))
            
    for length in list_b:
        if isinstance(length, (int, float)):
            combined_list.append(float(length))

    # If either input is empty or contains no valid numbers after filtering, handle gracefully. 
    # For this implementation, we assume inputs are lists of numeric lengths as per the task description.
    
    max_val = max(combined_list) if len(combined_list) > 0 else float('-inf')
    min_val = min(combined_list) if len(combined_list) > 0 else float('inf')

    # Calculate range difference (max - min) and return the results in a dictionary
    range_difference = max_val - min_val
    
    result_dict = {
        'max_combined': max_val,
        'min_combined': min_val,
        'range_difference': range_difference
    }
    
    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    lengths_group_a = [10.5, 22.3, 15.0]
    lengths_group_b = [8.7, 30.1, 14.9, 25.6]

    results = compare_length_lists(lengths_group_a, lengths_group_b)
    
    # Print the output for verification without requiring external input/files/network access
    print("Comparison Results:")
    print(f"Maximum Combined Length: {results['max_combined']}")
    print(f"Minimum Combined Length: {results['min_combined']}")
    print(f"Overall Range Difference: {results['range_difference']:.1f}")