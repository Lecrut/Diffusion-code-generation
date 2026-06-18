"""
Module to sort a list of tuples based on a custom key index in descending order.

This module provides functionality to take a list where each element is a tuple 
consisting of a value and an index, and sorts this list according to the values 
at a specified position (key_index) from right to left (descending).
"""

def sort_by_custom_rule(data_list: list[tuple], key_index: int) -> list[tuple]:
    """
    Sorts a list of tuples based on the value at the specified `key_index` in descending order.

    Args:
        data_list (list[tuple]): A list where each element is expected to be a tuple 
                                 containing at least two elements, representing (value, index).
        key_index (int): The integer position within each tuple that determines the sort order.

    Returns:
        list[tuple]: A new sorted list of tuples based on the values found at `key_index`.

    Raises:
        TypeError: If data_list is not a list or if any element in data_list is not a tuple.
        IndexError: If key_index exceeds the bounds of the elements within the tuples 
                   (i.e., len(tuple) <= key_index).

    Example:
        >>> sample_data = [(10, 2), (5, 3), (8, 4)]
        >>> result = sort_by_custom_rule(sample_data, 0)
        # Result will be sorted by the first element of each tuple in descending order.
        """
    if not isinstance(data_list, list):
        raise TypeError("The data_list argument must be a list.")

    for item in data_list:
        if not isinstance(item, tuple):
            raise TypeError(f"Each element in data_list must be a tuple, got {type(item).__name__}.")
    
    # Validate key_index against the structure of tuples to ensure it doesn't exceed bounds. 
    # We check at least one item's length for simplicity; if all items are identical length, this suffices.
    sample_len = len(data_list[0]) if data_list else 1
    if not isinstance(key_index, int):
        raise TypeError("The key_index argument must be an integer.")
    
    # Check that the provided index is within valid bounds for at least one tuple in the list.
    try:
        _ = data_list[0][key_index]
    except IndexError as e:
        raise IndexError(f"The specified key_index ({key_index}) exceeds the length of tuples (length {sample_len}).") from e

    # Sort using a lambda function to extract and compare values at `key_index` in descending order.
    return sorted(data_list, key=lambda x: x[key_index], reverse=True)

if __name__ == '__main__':
    # Hard-coded sample data for testing purposes without user input or external dependencies.
    sample_data = [
        (10, 2), 
        (5, 3), 
        (8, 4), 
        (9, 1)
    ]

    print("Original Data:", sample_data)

    # Sort by the first element of each tuple in descending order.
    sorted_by_first = sort_by_custom_rule(sample_data, key_index=0)
    print("\nSorted by index 0 (descending):", sorted_by_first)

    # Sort by the second element of each tuple in descending order.
    try:
        sorted_by_second = sort_by_custom_rule(sample_data, key_index=1)
        print("Sorted by index 1 (descending):", sorted_by_second)
    except IndexError as e:
        print(f"Error sorting by index 1: {e}")

    # Attempting to sort with an invalid index should raise an error.
    try:
        sorted_invalid = sort_by_custom_rule(sample_data, key_index=5)
    except IndexError as e:
        print("\nExpected Error for invalid index:", str(e))