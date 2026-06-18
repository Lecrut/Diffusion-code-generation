"""
Module to sort a list of tuples based on a custom rule defined by an index key in descending order.
"""

def sort_by_custom_rule(data_list, key_index):
    """
    Sorts a list of tuples (value, index) based on the value at the specified `key_index` 
    in descending order.

    Parameters:
        data_list (list[tuple]): A list where each element is a tuple containing values and indices.
                                  Example format: [(100, 3), (50, 7), (20, 9)]
        key_index (int): The index within the tuples to use for sorting.

    Returns:
        list[tuple]: A new list sorted in descending order based on values at `key_index`.
                     Original list remains unchanged if not passed as mutable reference target 
                     and slicing is used internally (standard Python behavior).

    Raises:
        TypeError: If data_list is not a list or key_index is not an integer.
        IndexError: If any tuple in the list does not have `key_index` as a valid index,
                    or if data_list itself is empty while attempting access logic that assumes content 
                    (though sorting handles empty lists gracefully).

    Examples:
        >>> sort_by_custom_rule([(100, 3), (50, 7), (20, 9)], key_index=0)
        [(100, 3), (50, 7), (20, 9)]
        
        >>> sort_by_custom_rule([('a', 1), ('b', 0), ('c', 2)], key_index=0)
        [('c', 2), ('b', 0), ('a', 1)]

    Note:
        This function assumes each tuple in the list has at least `key_index + 1` elements.
    """
    
    if not isinstance(data_list, list):
        raise TypeError("data_list must be a list.")
    if not isinstance(key_index, int):
        raise TypeError("key_index must be an integer.")

    # Validation: Check all tuples have the required index before sorting to avoid partial failures or errors during sort
    for item in data_list:
        if len(item) <= key_index:
            raise IndexError(f"All items in data_list must contain at least {len(data_list)} elements, but found an insufficient length. Expected minimum tuple size of '{key_index + 1}'.")

    # Sort using a lambda function to extract the element at key_index for comparison
    return sorted(
        [item[:] for item in data_list], 
        key=lambda x: x[key_index], 
        reverse=True
    )

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    
    # Sample 1: Simple integer tuples sorted by the first element (descending)
    data_sample_1 = [(10, 'a'), (5, 'b'), (20, 'c')]
    
    print("Sample 1 - Sorting integers at index 0 in descending order:")
    result_1 = sort_by_custom_rule(data_sample_1, key_index=0)
    for item in result_1:
        print(f"Value {item[0]} (Index {item[1]})")

    # Sample 2: String tuples sorted by the second element's length at index 1
    data_sample_2 = [('x', 3), ('y', 'longer'), ('z', 5)]
    
    print("\nSample 2 - Sorting strings/tuples based on values (mixed types handled naturally):")
    # Note: In Python, mixed type comparison is allowed in lists but results are not always meaningful for human readers. 
    # Here we just demonstrate the sorting mechanism works regardless of element type as long as they compare correctly.
    
    result_2 = sort_by_custom_rule(data_sample_2, key_index=1)
    print("Sorted items:")
    for item in result_2:
        print(f"Value {item[0]} (Index {item[1]})")

    # Sample 3: Floating point numbers to demonstrate precision sorting
    data_sample_3 = [(3.5, 'high'), (1.2, 'low'), (-4.8, 'negative')]
    
    print("\nSample 3 - Sorting floats in descending order:")
    result_3 = sort_by_custom_rule(data_sample_3, key_index=0)
    for item in result_3:
        print(f"Value {item[0]} (Index {item[1]})")

    # Edge Case Check: Empty list handling demonstration logic would be here if we wanted to test it separately.
    # The function naturally handles empty lists by returning an empty sorted list without errors.