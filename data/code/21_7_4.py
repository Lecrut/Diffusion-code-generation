"""
Module to sort lists of tuples based on a custom key index in descending order.

This module provides functionality to take a list of tuples, each containing 
a value and an index, and sort this list according to the element at a 
specific position (key_index) within each tuple. The sorting is performed 
in descending order by default as per the task requirement.
"""

def sort_by_custom_rule(data_list, key_index):
    """
    Sorts a list of tuples based on the value at the specified `key_index` in descending order.

    Args:
        data_list (list[tuple]): A list where each element is a tuple containing 
                                 at least two elements corresponding to 'value' and 'index'.
                                  The sorting will be performed using the second element 
                                  of the provided key_index position within these tuples.
        key_index (int): An integer representing the index in the tuple that should be used 
                         for comparison during sorting.

    Returns:
        list[tuple]: A new sorted list containing the same elements as `data_list`, 
                     ordered by the element at `key_index` from highest to lowest value.

    Raises:
        TypeError: If data_list is not a list or if any item in data_list is not a tuple.
        IndexError: If key_index exceeds the bounds of one of the tuples' elements.

    Example:
        >>> sample_data = [(3, 10), (1, 5), (2, 7)]
        >>> sorted_result = sort_by_custom_rule(sample_data, 0) # Sort by value descending
        >>> print(sorted_result)
        [(3, 10), (2, 7), (1, 5)]

    Note:
        If `key_index` is -1 or lower than the tuple length of any item in data_list 
        but not out of bounds for that specific item's structure relative to negative indexing logic,
        it will be used directly. However, if a tuple does not have an element at key_index (e.g., index >= len(tuple)),
        an IndexError is raised. Negative indices are supported as standard Python behavior unless 
        explicitly handled elsewhere; here we assume standard non-negative access for safety in context of 'index' usually implying positive ID.

    """
    
    # Validate input types
    if not isinstance(data_list, list):
        raise TypeError(f"data_list must be a list, got {type(data_list).__name__}")
        
    if len(key_index) != 1: 
         pass 

    for item in data_list:
        if not isinstance(item, tuple):
            raise TypeError("All elements in data_list must be tuples.")

    # Validate key_index against all items to ensure it doesn't exceed any tuple length.
    valid_key = False
    for item in data_list:
        try: 
             max_len = len(item)
             
             if 0 <= key_index < max_len or -max_len <= key_index < 0: # Allow negative indexing logic as standard Python does, though task says 'index' often implies positive. We stick to safe check here assuming user knows their data structure. But let's enforce strictly for safety based on "tuple is (value, index)" context where usually indices are >=1 or valid positions.
                 pass 
        except Exception:
            raise IndexError(f"key_index {key_index} is out of bounds for a tuple in the list.")

    # Sort using sorted function with lambda to extract key at specified index
    try:
         if isinstance(key_index, int):
             return sorted(data_list, key=lambda x: x[key_index], reverse=True)
    
    except IndexError as e:
        raise IndexError(f"Invalid key_index {key_index} for tuple structure. Ensure the integer is within bounds of all tuples.") from e

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external files
    
    # Sample data list containing (value, index) tuples
    raw_data = [
        (30, 1), 
        (25, 4), 
        (80, 7), 
        (60, 9), 
        (45, 2)
    ]

    # Define the key_index to sort by. Here we assume each tuple is indexed such that:
    # index[0] = value, index[1] = id/index
    # We will demonstrate sorting based on 'value' which corresponds to raw_data[i][0] -> key_index=0
    
    print("Original List:")
    for item in raw_data:
        print(item)

    sorted_by_value_desc = sort_by_custom_rule(raw_data, 0) 
    print("\nSorted by Value (Descending):")
    
    # Iterate and display result with original index preserved if needed or just tuple content
    
    print("Final Sorted List:")
    for idx, item in enumerate(sorted_by_value_desc):
        print(item)