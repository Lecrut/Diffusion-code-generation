def sort_pairs(pairs: list) -> list:
    """
    Sorts a list of (value, index) tuples based on the 'value' element in reverse order.

    This function takes an iterable containing pairs where each pair consists of two elements
    typically representing a value and its corresponding original index. It returns a new list
    with these pairs sorted such that larger values appear before smaller ones. If multiple
    items have the same value, their relative order is preserved (stable sort).

    Parameters:
        pairs (list): A list of tuples where each tuple has exactly two elements 
                      [value, index]. The 'index' element is not used for sorting but must 
                      be present in the output.

    Returns:
        list: A new sorted list of tuples [(val1, idx1), (val2, idx2), ...] ordered by value descending.

    Raises:
        TypeError: If input is not a list or if any element within a tuple does not have exactly two elements.

    Complexity Analysis:
        Time Complexity: O(n log n) due to the sorting operation performed on n items.
        Space Complexity: O(n) for storing the new sorted list, as no in-place modification 
                       is made to the input structure (a copy or reordering creates a separate result).

    Example:
        >>> sort_pairs([(3, 0), (1, 2), (5, 4)])
        [(5, 4), (3, 0), (1, 2)]
    """
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")

    for i, pair in enumerate(pairs):
        if len(pair) != 2:
            raise ValueError(f"Tuple at index {i} does not contain exactly two elements. Got {len(pair)} instead.")

    # Sort by the first element (value) of each tuple in descending order (-1 ensures reverse sort on positive values, 
    # but Python's default is ascending so we use key with negative or simply specify reverse=True).
    sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)

    return sorted_pairs

if __name__ == '__main__':
    sample_data = [(3.5, 1), (7, 4), (2, 0), (9, 8), (3.5, 2)]
    
    # Process the sample data using our function
    result = sort_pairs(sample_data)

    print("Original list:", sample_data)
    print("\nSorted list:")
    for item in result:
        print(f"({item[0]}, {item[1]})")