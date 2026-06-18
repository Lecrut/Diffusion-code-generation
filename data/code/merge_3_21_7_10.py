"""
Module for sorting lists of tuples based on a custom key index in descending order.

This module provides functionality to sort a list where each element is expected 
to be a tuple with at least `key_index + 1` elements (0-based). The sorting criteria
are determined by the value located at `key_index`.
"""

def sort_by_custom_rule(data_list, key_index):
    """
    Sorts a list of tuples based on the value at the specified index in descending order.

    Args:
        data_list (list[tuple]): A list containing tuples to be sorted. Each tuple 
                                 should contain enough elements so that accessing 
                                 `tuple[key_index]` does not raise an IndexError.
        key_index (int): The integer index within each tuple representing the sorting key.
                         For example, if a tuple is `(val1, val2)`, setting this to 0 sorts by `val1`.

    Returns:
        list[tuple]: A new sorted list based on the specified `key_index` in descending order.

    Raises:
        ValueError: If any element in `data_list` does not contain an item at `key_index`.
        TypeError: If `data_list` is not a list or if elements are not tuples/sequences suitable for indexing.
    
    Example:
        >>> data = [(3, 'a'), (1, 'b'), (4, 'c')]
        >>> sort_by_custom_rule(data, 0)
        [(4, 'c'), (3, 'a'), (1, 'b')]
    """
    if not isinstance(data_list, list):
        raise TypeError("The first argument must be a list.")

    for item in data_list:
        if not hasattr(item, '__getitem__'):
            raise TypeError(f"Expected tuple or sequence element in {data_list}.")
        
        # Check bounds before sorting to provide clear error messages
        if key_index < 0 or key_index >= len(item):
            raise ValueError(f"All elements must have at least index {key_index + 1} (size: {len(item)}). "
                           f"Element encountered with insufficient length.")

    # Sort by the value at `key_index` in descending order (-ve sign handles this)
    return sorted(data_list, key=lambda x: x[key_index], reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without external input.
    
    # Sample 1: Sorting tuples by the first element (value at index 0)
    sample_data_1 = [(3, "apple"), (1, "banana"), (4, "cherry")]
    
    # Sample 2: Sorting a more complex list where we sort by the second value at index 1
    sample_data_2 = [(-5, -10), (-2, -8), (0, 0), (3, 6)]
    
    print("Original List 1:", sample_data_1)
    result_1 = sort_by_custom_rule(sample_data_1, key_index=0)
    print("Sorted by index 0 (Desc):", result_1)

    print("\nOriginal List 2:", sample_data_2)
    
    # Note: We only have numeric data for demonstration to avoid potential float string issues in sort logic 
    # though standard comparison works. If we needed mixed types, the implementation still holds as long as they are comparable.
    result_2 = sort_by_custom_rule(sample_data_2, key_index=0)
    print("Sorted by index 0 (Desc):", result_2)

    # Example where sorting is based on a negative value at index 1 to ensure logic works regardless of data type nature 
    # as long as comparison operators are valid.
    sample_data_3 = [(1, -5), (2, -9)]
    print("\nOriginal List 3:", sample_data_3)
    
    result_3 = sort_by_custom_rule(sample_data_3, key_index=1)
    # Descending order of negative numbers: -5 > -9, so the first tuple should come before second in original list? 
    # Wait, descending means largest first. -5 is greater than -9. So (1, -5), then (2, -9).
    
    result_3_desc = sort_by_custom_rule(sample_data_3, key_index=1)
    print("Sorted by index 1 (Desc):", result_3_desc)