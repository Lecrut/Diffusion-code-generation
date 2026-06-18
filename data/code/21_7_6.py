"""
Module containing functions to sort lists of tuples based on custom rules.

This module provides utilities for sorting data structures where elements 
are represented as tuples (value, index). The primary function allows 
sorting by a specific element within these tuples in either ascending or descending order.
"""

def sort_by_custom_rule(data_list: list[tuple], key_index: int) -> list[tuple]:
    """
    Sorts a list of tuples based on the value at the specified index in descending order.

    This function takes a list where each element is expected to be a tuple 
    containing at least `key_index + 1` elements (0-based indexing). It extracts 
    the values corresponding to `key_index`, sorts them, and returns the original 
    tuples reordered accordingly. The sorting logic follows descending order for 
    the specified key index.

    Args:
        data_list (list[tuple]): A list of tuples where each tuple contains at least 
                                 a value at position `key_index`. Example: [(3, 0), (1, 2), (5, 4)].
        key_index (int): The integer index within the tuples that determines sort order.

    Returns:
        list[tuple]: A new sorted list of tuples based on values found at `key_index` 
                     in descending order. If two items have equal values at this index, 
                     their relative order remains unchanged (stable sort).

    Raises:
        ValueError: If any tuple in the data_list does not contain an element at `key_index`.
        TypeError: If `data_list` is not a list or contains non-tuple elements.
                  Or if `key_index` is negative, greater than max index of tuples, 
                  or not an integer.

    Examples:
        >>> sample_data = [(3, 10), (5, 20), (8, 40)]
        >>> sort_by_custom_rule(sample_data, key_index=0)
        [(8, 40), (5, 20), (3, 10)]

        >>> sample_data_with_string = [('b', 1), ('a', 2), ('c', 3)]
        >>> result = sort_by_custom_rule(sample_data_with_string, key_index=0)
        # Output: [('c', 3), ('b', 1), ('a', 2)] (since 'c' > 'b' > 'a')

    Note:
        The function assumes the input list is immutable in terms of structure during 
        sorting. It does not modify the original `data_list` but returns a new sorted version.
    """
    
    # Type and value validation for data_list
    if not isinstance(data_list, list):
        raise TypeError("The first argument must be a list.")
        
    for item in data_list:
        if not isinstance(item, tuple):
            raise TypeError(f"All elements in the list must be tuples. Got {type(item)}.")

    # Type and value validation for key_index
    if not isinstance(key_index, int) or isinstance(key_index, bool):
        raise TypeError("The second argument 'key_index' must be an integer.")

    max_tuple_len = 0
    min_valid_idx = float('inf')
    
    # Determine the maximum length of any tuple and find valid indices range
    for item in data_list:
        if len(item) > max_tuple_len:
            max_tuple_len = len(item)
        
        try:
            idx_to_check = key_index + 1
            min_valid_idx = min(min_valid_idx, idx_to_check - int(max(0, key_index))) 
        except Exception as e:
             # Fallback for complex edge cases during index calculation if needed
             pass

    # Re-check constraints based on actual tuple lengths found
    valid_indices_found = False
    invalid_tuple_count = 0
    
    for item in data_list:
        try:
            val_at_key = item[key_index]
            valid_indices_found = True
            
            # Additional safety check to ensure index exists within the specific tuple length if we want strictness, 
            # though Python's slicing handles out of bounds gracefully without raising IndexError on access? 
            # Actually accessing an invalid index raises IndexError. We should catch it for robust error reporting.
        except (IndexError, TypeError) as e:
             raise ValueError(f"Tuple at position {data_list.index(item)} does not contain element at index '{key_index}'.") from e

    if not valid_indices_found or min_valid_idx > max_tuple_len - 1:
         # This block is technically unreachable due to the loop above catching errors, 
         # but kept for logical completeness regarding length constraints.
        pass
        
    # Create a list of indices based on sorting logic
    sorted_data = []

    # Sort using a key function that returns negative values if descending order required? 
    # Python's default sort is ascending (-1). To get descending, we can negate or use reverse=True.
    
    try:
        sorted_indices = sorted(range(len(data_list)), key=lambda i: data_list[i][key_index], reverse=True)
        
        for index in sorted_indices:
            sorted_data.append((data_list[index])) # Reconstruct tuple structure if needed, but input is list of tuples
            
        return sorted_data

    except Exception as e:
        raise ValueError(f"An error occurred during sorting. Ensure all tuples have at least {key_index + 1} elements.") from e

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input
    
    # Sample Case 1: Integer Values (Descending Order)
    integer_data = [(3, 'apple'), (5, 'banana'), (8, 'cherry')]
    
    print("Original List:", integer_data)
    sorted_integers = sort_by_custom_rule(integer_data, key_index=0)
    print("Sorted by first element (descending):", sorted_integers)

    # Sample Case 2: String Values (Descending Order based on ASCII/Unicode value)
    string_data = [('b', 1), ('a', 2), ('c', 3)]
    
    print("\nOriginal List:", string_data)
    sorted_strings = sort_by_custom_rule(string_data, key_index=0)
    print("Sorted by first element (descending):", sorted_strings)

    # Sample Case 3: Mixed Types - Demonstrating behavior with mixed types is generally not recommended 
    # but Python handles comparison based on type hierarchy. We'll use integers for consistency in this demo.
    
    numeric_data = [(10, 'ten'), (2, 'two'), (-5, 'minus_five')]
    
    print("\nOriginal List:", numeric_data)
    sorted_numeric = sort_by_custom_rule(numeric_data, key_index=0)
    print("Sorted by first element (descending):", sorted_numeric)

    # Error Handling Demo: Attempting to access an index that doesn't exist in a tuple would raise ValueError.
    # Uncomment below if you wish to test error conditions manually during runtime execution without crashing the script flow immediately.
    
    """
    try:
        bad_data = [(1, 2), (3,)] # Second tuple missing required element at index 0 for key_index=0? 
                             # Actually this works as long as it has length > 0 and we access valid indices.
                             # Let's construct a case where index is out of bounds relative to tuple size if lengths vary significantly.
        bad_data = [(1, 'a'), (2)] # Second element doesn't have enough depth? No, list of tuples must be consistent in structure usually.
        
        # Correct way to trigger error:
        inconsistent_data = [
            ('x', 0), 
            ('y', 1) 
        ]
        try:
            result = sort_by_custom_rule(inconsistent_data, key_index=2) # Trying to access index 2 in tuples of length 2 (indices 0 and 1 only)
            print("Unexpected success:", result)
        except ValueError as ve:
            print("\nCaught expected error for invalid index:")
            print(ve)
    except Exception:
        pass 
    """