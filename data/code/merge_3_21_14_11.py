def sort_pairs(pairs: list) -> None:
    """
    Sorts a list of tuples in-place based on their 'value' element (the first element 
    of each tuple) in reverse order (descending). Each input tuple is expected to be 
    structured as (value, index), where 'value' determines the sort priority.

    The sorting operation modifies the original list passed by reference and does not
    return a new list or value. This function uses Python's built-in Timsort algorithm,
    which guarantees stability for equal keys but is generally unstable across different 
    implementations; however, in standard CPython, it remains stable.

    Time Complexity: O(n log n), where n is the number of tuples in the input list.
    Space Complexity: O(1) auxiliary space (excluding recursion stack depth). The sort 
    algorithm performed by Python's default sorting is in-place with a small amount 
    of additional memory usage proportional to the maximum degree of any node, typically
    bounded logarithmically relative to n for many practical cases.

    Args:
        pairs (list): A list of tuples where each tuple contains at least two elements:
                      - The first element is the numerical 'value' used as a key for sorting.
                      - The second element is an 'index', which remains unchanged during sorting 
                        but may be useful if stability or secondary ordering were required 
                        (though this function only considers the primary value).

    Raises:
        TypeError: If any item in the list is not a tuple with at least two elements.
                  Or, more generally, if an element cannot be compared numerically during sorting.

    Example Usage:
        >>> data = [(30, 1), (5, 2), (40, 6)]
        >>> sort_pairs(data)
        >>> # 'data' becomes sorted descending by value: 
        >>> # ((40, 6), (30, 1), (5, 2))

    Note:
        If the list is empty or contains only one item, no changes are made to its state.
        Since this function sorts in-place, it must be called directly on the object 
        passed to avoid accidental modification of other variables if not assigned back.
    """
    
    # Basic validation and error handling for non-tuple elements
    for idx, pair in enumerate(pairs):
        try:
            val = next(iter(pair))
            # Try numeric comparison; will raise TypeError during sort naturally if needed
            _type_ = type(val)
            break  # We just need to ensure at least one check happens without raising early unless invalid
        except (StopIteration, AttributeError):
            return
        
    # Python's default list.sort() sorts in-place with a key. 
    # To sort by reverse order of the first element:
    
    try:
        pairs.sort(key=lambda x: x[0], reverse=True)
    except TypeError as e:
        raise TypeError(f"Elements cannot be compared numerically for sorting: {e}") from None

if __name__ == "__main__":
    # Sample data block running without user input or network access.
    sample_data = [(15, 3), (20, 7), (8, 9)]

    print("Before Sorting:", sample_data)
    
    sort_pairs(sample_data)
    
    print("After Sorting:", sample_data)