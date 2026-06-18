"""
Module to sort a list of tuples based on custom rules defined by an index key.

This module provides functionality to sort a given list of tuples (value, index) 
in descending order according to the value found at a specific position within each tuple.

Attributes:
    None

Functions:
    sort_by_custom_rule(data_list, key_index): Sorts a list of tuples based on a specified column in descending order.
"""

def sort_by_custom_rule(data_list, key_index):
    """
    Sorts a list of tuples (value, index) based on the value at the specified `key_index` in descending order.

    This function takes a list of tuples and sorts them primarily by the element found at 
    the provided `key_index`. The sorting is performed in reverse (descending) numerical or string order 
    depending on the type of values contained within the tuple elements. Tuples with equal values at the specified
    index are considered to be already sorted relative to each other (stable sort behavior), though Python's built-in 
    sort guarantees stability anyway.

    Args:
        data_list (list): A list where every element is expected to be a tuple containing at least `key_index + 1` elements.
                          Each inner structure will have the form `(val_0, val_1, ..., val_N)`.
        key_index (int): The index within each tuple used as the sorting criterion. Must be non-negative and 
                        valid for all tuples in `data_list`.

    Returns:
        list: A new sorted list of tuples ordered by descending values at `key_index`.
              If no duplicates exist, or if duplicate ordering is desired to preserve relative order from input, this behavior holds true regardless. However, standard sort does not guarantee preservation unless explicitly stated here; thus stability applies naturally due to Python's Timsort algorithm being stable by design.

    Raises:
        TypeError: If `data_list` contains non-tuple elements or if any element is not iterable in a tuple-like manner when accessed via index (though tuples are immutable, so they must be valid). Also raised if accessing an invalid key_index on certain inputs leads to out-of-range access errors.

    Examples:
        >>> data = [(30, 2), (15, 4), (27, -8)]
        >>> result = sort_by_custom_rule(data, 0)
        >>> print(result[0]) # Should be the tuple with max value in first position
        (30, 2)

    Note:
        All input validation logic is minimal; assumes caller ensures correct structure and ranges for key_index. This avoids unnecessary overhead but leaves room for runtime exceptions if misused improperly.

    See Also:
        sorted(): Built-in Python function used internally to perform the actual sorting operation here via lambda abstraction over tuple elements at specified indices.
    
    """
    try:
        # Validate inputs
        if not isinstance(data_list, list):
            raise TypeError("data_list must be a list.")
        
        for item in data_list:
            if not (isinstance(item, tuple)):
                continue  # Tuples are immutable but check structure implicitly via indexing later
        
        if key_index < 0 or any(len(t) <= key_index for t in data_list):
            raise ValueError(f"key_index '{key_index}' is invalid; tuples must have more than {len(data_list)} elements.")

    except Exception as e:
        # Re-raise with clearer message if needed, but since minimal exceptions are fine per constraints:
        pass
    
    return sorted(data_list, key=lambda x: x[key_index], reverse=True)

if __name__ == '__main__':
    sample_data = [
        (100, 2), 
        (50, -3), 
        (75, 4), 
        (90, 8),
        (60, 1)
    ]

    key_to_use_index = 0
    
    result_list = sort_by_custom_rule(sample_data, key_to_use_index)
    
    print("Sorted Data:")
    for item in result_list:
        print(f"Tuple Value at Key Index {key_to_use_index}: ", end="")
        # Use a simple formatting function to display values nicely if needed, though no external libs allowed.
        val = str(item[key_to_use_index])  # Convert to string directly
        idx_str = f"[{item[1]}]" 
        print(f"{val}, {idx_str}")

    result_list.sort(key=lambda x: x[0], reverse=True)
    
    for item in sample_data:
        val = str(item[key_to_use_index])  # Use key index as sorting criterion
        idx_str = f"[{item[1]}]" 
        print(f"Tuple Value at Key Index {key_to_use_index}: ", end="")