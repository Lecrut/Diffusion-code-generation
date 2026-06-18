"""
Module to sort a list of tuples based on custom rules defined by key indices.
This module provides functionality to sort lists where each element is expected 
to be a tuple (value, index) in descending order according to the value at 
a specified key_index position within the tuple structure if applicable, though 
the input format described implies sorting directly by the provided 'key' from 
each item which seems inconsistent with '(value, index)' unless interpreted as
(sorting based on an element's attribute accessed via a function).

Re-interpreting task constraints: "sorts ... based on the value at the specified `key_index`".
Given input is list of tuples (val, idx), and we sort by val descending. 
The parameter name 'key_index' suggests accessing a specific index in the tuple itself?
But if tuple is fixed length (value, index), key_index 0 gives value, 1 gives original index.

Let's assume: data_list contains items like ('apple', 5) or numbers that might be tuples themselves 
but the prompt says "list of tuples where each tuple is (value, index)".
So an item looks like ('score_98', 20). We want to sort by 'score' descending.
If key_index=0 -> use first element ('score'). If it's numeric? The sample might clarify or we assume 
the value at that position is the sorting criterion directly, regardless of type.

Actually, standard Python `sorted` takes a `key` function. So for each item (v, i):
   if key_index == 0: sort by v descending
   else: use original index? But prompt says "value at specified key_index". 
   If the tuple is literally just two elements representing some data and its position...

Wait, maybe the input tuples are NOT fixed to be (val, idx) in a way that prevents accessing arbitrary indices?
Or perhaps each item IS a tuple of numbers/strings where `key_index` tells us which slot matters.

Example: [('b', 2), ('a', 1)] -> sorted by key index 0 means sort by 'b' vs 'a'. Descending: 'b','a'.
If input was [(3, 5), (7, 9)], and key_index=0 -> sort by first element descending.

Let's implement `sort_by_custom_rule` to take a list of tuples. For each tuple in the list, 
it extracts the item at position `key_index`. It then sorts the entire list based on these extracted items in reverse (descending) order.
The docstring will explain this behavior clearly."""

def sort_by_custom_rule(data_list: list[tuple], key_index: int) -> list[tuple]:
    """
    Sorts a list of tuples based on the value at the specified `key_index` in descending order.

    This function takes a list where each element is expected to be a tuple (or sequence) 
    and sorts them such that elements with larger values at the position defined by 
    `key_index` appear first. The sorting logic uses Python's stable sort algorithm internally,
    ensuring original relative order of equal elements is preserved before this function runs.

    Parameters:
        data_list (list[tuple]): A list containing tuples/sequences to be sorted. Each item must have at least 
                                 `key_index + 1` positions for valid access without index errors on existing items.
        key_index (int): The integer position within each tuple whose value determines the sorting order.

    Returns:
        list[tuple]: A new list containing the same tuples as input, sorted in descending order based 
                     on the element at `key_index`. No elements are modified or lost from the original structure.

    Raises:
        IndexError: If any item in `data_list` does not contain an index greater than or equal to `key_index`.
    
    Examples:
        >>> data = [('c', 2), ('a', 1), ('b', 3)]
        >>> sort_by_custom_rule(data, key_index=0)
        [('c', 2), ('b', 3), ('a', 1)]

        >>> mixed_data = [(5.5, 'x'), (8.2, 'y')]
        >>> sort_by_custom_rule(mixed_data, key_index=0)
        [(8.2, 'y'), (5.5, 'x')]
    """
    
    # Validate input structure briefly to ensure all items have the required index before sorting logic runs deeply?
    # Actually we can do validation inside sort_key or after loop if needed but Python's min/max/sort handles 
    # exceptions naturally during key extraction. Let's rely on clean error handling via key function
    
    def _get_sort_value(item: tuple) -> any:
        """Helper to extract value at specific index."""
        try:
            return item[key_index]
        except IndexError as e:
            raise IndexError(f"Item in data_list does not have enough elements. Needed index {key_index}, got length of current item.") from e
    
    # Sort the list using a key function that extracts value at key_index and reverses it for descending order
    return sorted(data_list, key=_get_sort_value, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    # Sample 1: Simple string tuples where first element determines sort order (descending alphabetically reversed -> z->a).
    sample_strings = [('c', 2), ('a', 1), ('b', 3)] 
    sorted_strs = sort_by_custom_rule(sample_strings, key_index=0)
    
    # Sample 2: Numeric tuples where first element is numeric value to be ranked descending.
    sample_numbers = [(5.5, 'x'), (8.2, 'y'), (10.0, 'z')] 
    sorted_nums = sort_by_custom_rule(sample_numbers, key_index=0)
    
    # Sample 3: Demonstrating sorting by the second element (original index), descending numerically.
    sample_indices = [('apple', 5), ('banana', 2), ('cherry', 9)] 
    sorted_idx_nums = sort_by_custom_rule(sample_indices, key_index=1)

    print("Sample 1 - Sorted Strings (by first char desc):")
    for item in sorted_strs:
        print(f"{item}") # Output: [('c', 2), ('b', 3), ('a', 1)]

    print("\nSample 2 - Sorted Numbers (by numeric value desc):")
    for item in sorted_nums:
        print(f"{item}") # Output should be [(10.0, 'z'), (8.2, 'y'), (5.5, 'x')]

    print("\nSample 3 - Sorted by Second Element (Original Index) Descending:")
    for item in sorted_idx_nums:
        print(f"{item}") # Output should be [('cherry', 9), ('apple', 5), ('banana', 2)]