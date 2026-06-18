def compare_length_lists(list1: list[float], list2: list[float]) -> dict:
    """
    Compares two lists of length measurements to determine maximums, minimums,
    and overall range difference.

    Args:
        list1 (list[float]): First list of numerical lengths.
        list2 (list[float]): Second list of numerical lengths.

    Returns:
        dict: A dictionary containing 'max_list1', 'min_list1', 
              'max_list2', 'min_list2', and 'range_difference'.
    
    Raises:
        ValueError: If either input list is empty or contains non-numeric data.
    """
    # Validation for List 1
    if not list1 or any(not isinstance(x, (int, float)) for x in list1):
        raise ValueError("List 1 must contain numeric values and cannot be empty.")

    max_l1 = max(list1)
    min_l1 = min(list1)
    
    # Validation for List 2
    if not list2 or any(not isinstance(x, (int, float)) for x in list2):
        raise ValueError("List 2 must contain numeric values and cannot be empty.")

    max_l2 = max(list2)
    min_l2 = min(list2)
    
    # Calculate range difference as the absolute difference between 
    # the maximum of both lists combined (or just summing ranges? Task implies overall context).
    # Interpretation: "Overall range" usually means Max(Combined) - Min(Combined).
    all_lengths = list1 + list2
    global_max = max(all_lengths)
    global_min = min(all_lengths)
    
    return {
        'max_list1': max_l1,
        'min_list1': min_l1,
        'max_list2': max_l2,
        'min_list2': min_l2,
        'range_difference': (global_max - global_min), # Absolute difference between extremes of combined set
    }

if __name__ == '__main__':
    sample_data_1 = [5.0, 8.2, 3.7, 9.1]
    sample_data_2 = [4.5, 6.0, 10.2, 2.8]

    result = compare_length_lists(sample_data_1, sample_data_2)
    
    print("Comparison Results:")
    print(f"List 1 Max: {result['max_list1']}")
    print(f"List 1 Min: {result['min_list1']}")
    print(f"List 2 Max: {result['max_list2']}")
    print(f"List 2 Min: {result['min_list2']}")
    print(f"Overall Range Difference (Combined): {result['range_difference']:.4f}")