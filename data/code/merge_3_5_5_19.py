def compare_length_lists(list_a, list_b):
    """
    Compares two lists of length measurements to determine:
        - Maximum value present in either list (max_len)
        - Minimum value present in either list (min_len)
    
    Returns a dictionary containing these values and the overall range difference.
    If input lists are empty, raises ValueError with an appropriate message.
    """
    if not list_a or not list_b:
        raise ValueError("At least one of the provided lists must be non-empty.")

    # Combine both lists to find global max/min across all inputs
    combined_lengths = list_a + list_b
    
    try:
        min_len = min(combined_lengths)
        max_len = max(combined_lengths)
    except ValueError as e:
        raise ValueError(f"Invalid length values provided (must be numeric): {e}")

    range_difference = max_len - min_len

    return {
        "max_length": max_len,
        "min_length": min_len,
        "range_difference": range_difference
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    measurements_group_a = [10.5, 23.4, 15.7]
    measurements_group_b = [8.9, 30.2, 12.1]

    result = compare_length_lists(measurements_group_a, measurements_group_b)

    print("Length Comparison Report:")
    print(f"Maximum Length: {result['max_length']}")
    print(f"Minimum Length: {result['min_length']}")
    print(f"Overall Range Difference: {result['range_difference']}")