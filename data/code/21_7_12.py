"""
Module to sort a list of tuples based on a custom key index in descending order.

This module provides functionality to take a list where each element is expected 
to be a tuple containing at least two elements: (value, index). The sorting logic
ignores the 'index' part during comparison and sorts strictly by the 'value'.

The function returns a new sorted list without modifying the original input.
"""

def sort_by_custom_rule(data_list, key_index):
    """
    Sorts a list of tuples based on the value at the specified `key_index` in descending order.

    Args:
        data_list (list[tuple]): A list where each element is expected to be a tuple 
            with structure (value, index). The 'index' component is ignored during sorting;
            only the first component ('value') corresponding to key_index=0 logic applies 
            generally if we assume standard 2-tuples. However, this function generalizes:
            It extracts the element at `key_index` from each tuple for comparison purposes.
            
        key_index (int): The index within each tuple that determines the sort order.

    Returns:
        list[tuple]: A new list containing tuples sorted in descending order based on 
            the value found at `data_list[i][key_index]`.

    Raises:
        IndexError: If a tuple does not have an element at the specified `key_index`.
        TypeError: If `data_list` is not a list or contains non-tuple elements.

    Example:
        >>> data = [(10, 5), (3, 2), (7, 8)]
        >>> sort_by_custom_rule(data, 0)
        [(10, 5), (7, 8), (3, 2)]
        
        Note: If the tuple structure is different or key_index refers to a non-first element,
        ensure tuples are large enough. This implementation assumes standard behavior where 
        sorting relies on data_list[i][key_index]. For typical use cases described in task,
        it effectively sorts by value if key_index=0 (assuming first element is the primary sort key).

    """
    
    # Validate input types
    if not isinstance(data_list, list):
        raise TypeError("data_list must be a list.")
        
    for item in data_list:
        if not isinstance(item, tuple):
            raise TypeError(f"All elements in data_list must be tuples. Found {type(item).__name__}.")

    # Check validity of key_index against all items to avoid runtime errors during sort
    min_len = len(data_list) and min(len(t) for t in data_list if isinstance(t, tuple)) or 0
    
    if key_index < 0 or key_index >= min_len:
        raise IndexError(f"key_index ({key_index}) is out of range for the provided tuples (min length {min_len}).")

    # Sort using a lambda function that extracts and compares based on key_index
    sorted_list = sorted(data_list, key=lambda item: item[key_index], reverse=True)
    
    return sorted_list

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    # Sample data consists of tuples (value, index). 
    # We will test sorting by the first element (index 0), which represents 'value'.
    raw_data = [
        (15, 42),
        (3, 9),
        (7, 18),
        (15, 6),   # Tie-breaker: stable sort usually keeps original order for equal keys.
        (0, 1)
    ]

    print("Original List:")
    for item in raw_data:
        print(f"({item[0]}, {item[1]})")

    sorted_result = sort_by_custom_rule(raw_data, key_index=0)

    print("\nSorted List (Descending by value):")
    for item in sorted_result:
        print(f"({item[0]}, {item[1]})")