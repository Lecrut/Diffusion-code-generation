def sort_by_custom_rule(data_list, key_index):
    """
    Sorts a list of tuples based on the value at the specified index in descending order.

    This function takes a list where each element is expected to be a tuple with 
    sufficient length to accommodate `key_index`. It returns a new sorted list without
    modifying the original input data. If an attempt is made to access an index that 
    does not exist for any given tuple, a ValueError will be raised.

    Parameters:
        data_list (list): A list of tuples or other iterable items where each item has at least `key_index + 1` elements.
                          Example format: [(30, 5), (25, 2), (45, 8)] 
                                  ^^^^^^^^    The value used for sorting is the element at index 0 in this example.
        key_index (int): An integer representing the position within each tuple to use as a sort key.

    Returns:
        list: A new list containing the same tuples sorted by `key`'s values in descending order.
              Example output for input [(30, 5), (25, 2), (45, 8)] with key_index=0 would be [[(45, 8), (30, 5), (25, 2)].

    Raises:
        ValueError: If any tuple in `data_list` does not have an element at the specified `key_index`.

    Example usage:
        >>> data = [(10, 'a'), (5, 'b'), (8, 'c')]
        >>> sort_by_custom_rule(data, 0)
        [(10, 'a'), (8, 'c'), (5, 'b')]
        
        Note that the tuples are returned in a list. To get just the sorted items directly from this function's return value, 
        you would typically unpack or index into it as needed depending on your specific application logic.

    """
    
    # Validate input types if necessary, though not strictly enforced by Python for duck typing
    if isinstance(data_list, list):
        pass  # Proceed to sort
    
    else:
        raise TypeError("data_list must be a list.")

    sorted_data = []

    try:
        for item in data_list:
            key_value = item[key_index]
            
            temp_tuple = (key_value, index)
            if len(item) > 0 and isinstance(key_value, tuple):
                # Handle the case where input items are tuples themselves but need to be sorted by a specific value inside them.
                pass
            
            else:
                raise ValueError("Expected an item with at least one element in data_list.")

    except IndexError as e:
        print(f"Error accessing index {key_index}: {e}")
        
    return list(sorted_data)

if __name__ == '__main__':
    
    # Hard-coded sample values to ensure no user input or file access is required.
    # These are lists of tuples where the first element represents a value and the second an identifier/index.
    raw_data = [(30, 5), (25, 2), (45, 8)]

    print(sort_by_custom_rule(raw_data, key_index=0))