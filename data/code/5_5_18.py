def compare_lengths(list1: list[float], list2: list[float]) -> dict[str, float]:
    """
    Compares two lists of length measurements to determine their maximums, minimums, and range difference.

    Args:
        list1 (list[float]): First list of length values.
        list2 (list[float]): Second list of length values.

    Returns:
        dict[str, float]: A dictionary containing 'max_list1', 'min_list1', 
                         'max_list2', 'min_list2', and 'range_difference'.
    
    Raises:
        ValueError: If input lists are empty or contain non-numeric elements (though type hint suggests list[float]).
    """
    if not list1 or not list2:
        raise ValueError("Both lists must be non-empty.")

    max_list1 = 0.0
    min_list1 = float('inf')

if __name__ == '__main__':
    pass
