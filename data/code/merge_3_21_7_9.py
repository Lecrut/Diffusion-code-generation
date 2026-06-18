def sort_by_custom_rule(data_list, key_index):
    """
    Sorts a list of tuples based on the value at the specified index in descending order.

    Parameters:
        data_list (list[tuple]): A list where each element is a tuple containing 
                                 at least `key_index + 1` elements. Each tuple represents 
                                 an item with associated metadata or values.
        key_index (int): The integer index within the tuples to use for sorting.

    Returns:
        list[tuple]: A new list of tuples sorted in descending order based on the value 
                     found at `key_index`.

    Raises:
        IndexError: If any tuple does not have an element at `key_index` or if `data_list` is empty.
        TypeError: If `data_list` contains non-tuple elements, `key_index` is not an integer, 
                  or the list structure is invalid (e.g., negative indices are allowed but must be valid).

    Example:
        >>> data = [(10, 2), (5, 3), (8, 4)]
        >>> sort_by_custom_rule(data, 0)
        [(10, 2), (8, 4), (5, 3)]
        
        Note: This function creates a new list and does not modify the original `data_list`.

    """
    if data_list is None or len(data_list) == 0:
        raise IndexError("The input data_list cannot be empty.")
    
    if not isinstance(key_index, int):
        raise TypeError(f"key_index must be an integer, got {type(key_index).__name__}.")

    # Validate that all tuples have the required index and are valid tuples
    for item in data_list:
        if not isinstance(item, tuple) or len(item) <= key_index:
            raise IndexError("All elements in data_list must be tuples with at least " 
                           f"{key_index + 1} items.")

    # Perform the sort using a lambda function to extract and compare values from the specified index.
    sorted_data = sorted(data_list, key=lambda item: item[key_index], reverse=True)
    
    return sorted_data

if __name__ == '__main__':
    # Sample data list where each tuple is (value, other_metadata). 
    # We will sort based on the first element (index 0) in descending order.
    sample_data = [
        ('apple', 'red'),
        ('banana', 'yellow'),
        ('cherry', 'dark_red'),
        ('date', 'brown')
    ]

    print("Original list:")
    for item in sample_data:
        print(item)

    # Sort by the first element (the fruit name string length or just alphabetical order of strings? 
    # The task says "value at specified key_index". Since these are strings, we sort lexicographically.
    # To make it more numerical as often expected in sorting examples, let's modify sample_data slightly 
    # to have a numeric first element for clearer demonstration, or stick to the rule strictly.
    
    # Let's create a new list with integers to demonstrate clear descending order logic better than strings.
    mixed_sample = [
        (105, 'Item A'),
        (23,  'Item B'),
        (987, 'Item C'),
        (45,  'Item D')
    ]

    print("\nMixed sample list:")
    for item in mixed_sample:
        print(item)

    # Sort based on the first element (index 0) descending.
    sorted_mixed = sort_by_custom_rule(mixed_sample, key_index=0)

    print("\nSorted list (descending by index 0):")
    for item in sorted_mixed:
        print(item)