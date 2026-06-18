"""
Module containing a custom sorting function for lists of tuples.

This module provides functionality to sort a list of tuples based on a specific index within each tuple,
in descending order by value. The implementation ensures stability and handles edge cases such as negative values or empty inputs gracefully.
"""

def sort_by_custom_rule(data_list: list[tuple], key_index: int) -> list[tuple]:
    """
    Sorts a list of tuples based on the value at a specified index in descending order.

    This function takes an iterable collection containing homogeneous elements (tuples), and returns 
    a new sorted version where each tuple's ordering is determined by its element found at 'key_index'.
    
    Parameters:
        data_list (list[tuple]): A list of tuples, where each tuple contains the value to be compared.
                                 The length of the tuple must match key_index + 1 or greater.
        key_index (int): An integer representing the index within each tuple that determines sorting order.

    Returns:
        list[tuple]: A new list containing the same tuples as input, but sorted in descending 
                     order based on the value at 'key_index'. The original list remains unmodified if not passed by reference and modified internally (though typically lists are mutable objects).
    
    Raises:
        TypeError: If data_list is not a list or key_index is not an integer.
        IndexError: If any tuple in the list does not have enough elements to access 'key_index'.

    Examples:
        >>> sample_data = [(4, 1), (2, 0), (8, 3)]
        >>> sort_by_custom_rule(sample_data, 0)
        [(8, 3), (4, 1), (2, 0)]
        
        Note: The original list is modified in place if passed directly. To avoid side effects, 
              consider creating a copy before passing to this function or calling it with the data_list reference carefully.

    Complexity Analysis:
        Time Complexity: O(n log n) due to sorting operations on 'n' items, where each item comparison takes constant time relative to tuple size.
        Space Complexity: O(1) if modifying input list in-place; otherwise O(n) for creating a new sorted copy when used with reverse=True logic or similar approaches internally without explicit copying of the entire structure before sort unless necessary (Python's Timsort is optimized).

    """
    
    # Input validation ensures type integrity and prevents runtime errors during execution.
    if not isinstance(data_list, list):
        raise TypeError(f"data_list must be a list, got {type(data_list).__name__}.")
    if not isinstance(key_index, int):
        raise TypeError(f"key_index must be an integer, got {type(key_index).__name__}.")

    # Iterates through the data_list to verify that each tuple contains at least key_index + 1 elements.
    for item in data_list:
        if not isinstance(item, tuple) or len(item) <= key_index:
            raise IndexError(f"Tuple {item} does not have enough elements for index {key_index}.")

    # Sorts the list using Timsort algorithm with a custom lambda function to extract values at 'key_index'.
    # The reverse parameter ensures descending order. Python's stable sort preserves relative order of equal keys.
    sorted_data = sorted(data_list, key=lambda x: x[key_index], reverse=True)

    return sorted_data

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or dependencies.
    # Sample data consists of tuples (value, index). Sorting by the first element in descending order is demonstrated here.
    raw_input = [
        (10, 5), 
        (2, 3), 
        (8, 7), 
        (6, 9)
    ]

    # Define key_index as 0 to sort based on the tuple's first element (the value).
    target_key_idx = 0
    
    # Call the main sorting function with validated inputs.
    result_list = sort_by_custom_rule(raw_input, target_key_idx)
    
    # Display sorted results for verification purposes within a simple print block.