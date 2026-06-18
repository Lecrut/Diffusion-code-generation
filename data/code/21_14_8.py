def sort_pairs(pairs: list) -> list:
    """
    Sorts a list of (value, index) tuples in reverse order based on the 'value' element.

    This function takes an input list where each item is expected to be a tuple containing 
    two elements: the first being a numeric value and the second being its associated index.
    The sorting operation prioritizes descending numerical values of these pairs, while maintaining
    stability for equal values if applicable (though standard Python sort is stable by default).

    Parameters:
        pairs (list): A list of tuples where each tuple has exactly two elements representing 
                      a value and an index respectively. Example format: [(10, 2), (5, 0), (8, 3)].

    Returns:
        list: A new list containing the same number of sorted tuples ordered by descending values.

    Raises:
        TypeError: If 'pairs' is not a list or if any element within 'pairs' is not a tuple 
                  with exactly two elements where both are numeric (int/float).

    Time Complexity: O(n log n), where n is the number of tuples in the input list, due to sorting.
    Space Complexity: O(n) for storing the returned sorted list and any internal sort structures used by Python's Timsort algorithm.
    
    Example usage:
        >>> data = [(50, 1), (20, 3), (80, 4)]
        >>> result = sort_pairs(data)
        >>> print(result)
        [(80, 4), (50, 1), (20, 3)]

    Note: This function does not modify the original list; it returns a new sorted list.
    """
    
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")
        
    for i, item in enumerate(pairs):
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError(f"Each element at index {i} must be a tuple with exactly two elements.")
            
        val, idx = item
        
        # Ensure both value and index are numeric types (int/float)
        try:
            float(val), int(idx)
        except TypeError as e:
            raise ValueError(f"Invalid content in pair at index {i}: values must be numeric. Got '{val}'") from e
            
    return sorted(pairs, key=lambda x: -x[0])

if __name__ == '__main__':
    # Sample data with (value, index) tuples for testing purposes only.
    sample_data = [
        (15, 2),
        (30, 7),
        (45, 9),
        (60, 4),
        (85, 11),
        (25, 5)
    ]

    # Display original data before sorting
    print("Original list:", sample_data)

    # Perform the sort operation
    sorted_result = sort_pairs(sample_data)

    # Display result after sorting in descending order of values
    print("Sorted list:", sorted_result)