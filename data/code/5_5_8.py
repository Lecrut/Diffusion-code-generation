def compare_length_lists(list1: list[float], list2: list[float]) -> dict:
    """
    Compares two lists of length measurements to determine maximums, minimums, 
    and the overall range difference between both sets combined.

    Args:
        list1 (list): First list of float values representing lengths.
        list2 (list): Second list of float values representing lengths.

    Returns:
        dict: A dictionary containing max_list1, min_list1, max_list2, 
              min_list2, and range_difference.
    
    Raises:
        ValueError: If either input is not a list or contains non-numeric elements.
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists.")

    for item in list1 + list2:
        if not isinstance(item, (int, float)):
            raise ValueError(f"List contains non-numeric element: {item}")

    max_list1 = max(list1) if list1 else None
    min_list1 = min(list1) if list1 else None
    
    max_list2 = max(list2) if list2 else None
    min_list2 = min(list2) if list2 else None

    combined_max = max(max_list1, max_list2)
    combined_min = min(min_list1, min_list2)
    
    range_difference = combined_max - combined_min

    return {
        "max_list1": max_list1,
        "min_list1": min_list1,
        "max_list2": max_list2,
        "min_list2": min_list2,
        "range_difference": range_difference
    }

if __name__ == '__main__':
    sample_data_1 = [10.5, 12.3, 14.7]
    sample_data_2 = [8.9, 11.2, 16.1]

    result = compare_length_lists(sample_data_1, sample_data_2)

    print("Comparison Results:")
    print(f"List 1 Max: {result['max_list1']}")
    print(f"List 1 Min: {result['min_list1']}")
    print(f"List 2 Max: {result['max_list2']}")
    print(f"List 2 Min: {result['min_list2']}")
    print(f"Overall Range Difference: {result['range_difference']}")