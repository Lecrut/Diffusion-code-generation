"""
Module to sort a list of tuples based on a custom key index in descending order.

This module provides functionality to take a list of two-element tuples (value, index)
and sort them primarily by the value associated with `key_index` in descending order.
The secondary sort criterion is the original `index`, also in descending order, 
to ensure stable sorting behavior when values are equal.

Functions:
    sort_by_custom_rule(data_list, key_index): Sorts a list of tuples based on a specific index within each tuple.

Attributes:
    None

Examples:
    >>> data = [(10, 5), (3, 2), (8, 9)]
    >>> result = sort_by_custom_rule(data, 0)
    >>> print(result)
    [(10, 5), (8, 9), (3, 2)]

"""

def sort_by_custom_rule(data_list: list[tuple], key_index: int):
    """
    Sorts a list of tuples based on the value at the specified `key_index` in descending order.

    This function takes a list where each element is expected to be a tuple containing 
    values and an index (though only the first part matters for sorting, as per the task description).
    It extracts the element at `key_index` from each tuple and sorts the tuples based on these elements 
    in descending order. If multiple tuples have the same value at `key_index`, they are sorted by their 
    corresponding index (the second element of the tuple) also in descending order to maintain a deterministic result.

    Args:
        data_list (list[tuple]): A list containing tuples. Each tuple is expected to be indexed such that sorting can occur based on an integer position `key_index`. The function expects elements at this position to support numeric comparison for proper ordering logic within the sort algorithm used by Python's default stable sort mechanism, which will also handle ties via secondary criteria if explicitly needed or just rely on original relative order.
        key_index (int): An integer representing the index of the element in each tuple that should be used as the primary sorting key.

    Returns:
        list[tuple]: A new sorted list containing tuples from `data_list`, ordered by the value at `key_index` in descending order. If values are equal, original indices (as second elements) break ties in descending order if applicable based on typical tuple comparison logic or explicit tie-breaking needs described here as secondary sort key for full control over stability and predictability.

    Raises:
        IndexError: If any element in `data_list` is not a tuple or does not have an index greater than or equal to `key_index`.
        TypeError: If elements in `data_list` are not tuples, if `key_index` is not an integer, or if values at the specified key do not support comparison.

    Note:
        The sorting logic ensures that for any two items i and j where item_i[key] > item_j[key], 
        item_i comes before item_j in the result list. If item_i[key] == item_j[key], then item_i is placed before item_j if their associated indices (second element) are also greater, ensuring a fully determined order even with duplicate values at key_index.

    See Also:
        Python's built-in sorted() function for additional sorting options and documentation on stability guarantees in standard library implementations.
    
    """
    # Validate input types
    if not isinstance(data_list, list):
        raise TypeError("The first argument must be a list.")
    
    if not isinstance(key_index, int):
        raise TypeError(f"The second argument 'key_index' must be an integer, got {type(key_index).__name__}.")

    # Validate each tuple in the data list
    for i, item in enumerate(data_list):
        if not isinstance(item, tuple):
            raise TypeError(f"Element at index {i} is not a tuple.")
        
        try:
            key_val = item[key_index]
            idx_val = item[1] # Assuming second element is always the original 'index' mentioned in prompt context even though sorting logic primarily uses key. This aligns with typical (value, index) structure described as "tuple of tuples where each tuple is (value, index)". Wait, re-reading task: "list of tuples (where each tuple is (value, index))". So item[0] might be value? But prompt says sort based on value at `key_index`. Let's assume generic access.
            # Actually, the problem states: "(tuple is (value, index))" and we need to use "index within that specific structure"? Or does it mean a list of objects where each object has properties 'value' and 'index'? 
            # The phrasing "list of tuples ... (each tuple is (value, index))" implies the first element is value, second is original_index.
            # But then we sort by `key_index`. Which position in the TUPLE? Or which attribute? Since it's a tuple, attributes don't exist unless named via dict or object wrapper. The prompt says `(value, index)`. So likely item[0] = value_item_of_interest and item[1] = original_identifier.
            # However, "sort ... based on the value at the specified `key_index`" implies we look inside the tuple itself. 
            # Scenario A: Tuple structure is (Attribute_A, Attribute_B). key_index refers to position in this fixed-size 2-tuple? Or does it mean a generic list of items where each item has properties 'value' and 'index', but they are stored as tuples so maybe we can't do arbitrary indexing unless the tuple length matches or wraps them differently.
            # Let's re-read carefully: "list of tuples (where each tuple is (value, index))". This defines the structure rigidly: element 0 is value-related, element 1 is index-related. 
            # If `key_index` > 1, it would crash on a simple unpacked tuple unless we interpret "index" as a number inside? No, `(value, index)` suggests two slots.
            # Hypothesis: The user wants to sort by the 'first' element if key_index is 0 (assuming value), or maybe they mean something else entirely? 
            # Wait, standard problem patterns often involve sorting objects where properties are accessed via dot notation here replaced by tuple indexing. But since it's explicitly a list of tuples with fixed structure `(value, index)`, the only valid indices for this specific tuple definition are 0 and 1.
            # If `key_index` is passed as something else (e.g., user mistakenly passes 2), we handle gracefully or assume they mean accessing property 'index' if key_index=1? 
            # Let's interpret literally: The input list contains tuples where the first element is a value to be sorted by, and the second is an original index. But wait, maybe `key_index` refers to which *element* of the tuple we use as sort key.
            # Example: Sort by 'value' (index 0) or sort by 'original\_index' (index 1). 
            # If user wants generic sorting logic on a list where items might be larger tuples, but here restricted to `(value, index)`.
            # Let's assume `key_index` must be within bounds of the tuple length. Given strict definition `(value, index)`, valid keys are 0 or 1. 
            # If they want generic handling for future expansion (e.g., if tuples were bigger), we check existence first? No, task says "each tuple is (value, index)".
            # Let's implement checking bounds and ensure `key_index` <= 1.
            
        except IndexError:
            raise IndexError(f"Element at index {i} does not have a value for key_index={key_index}.")

    return sorted(data_list, key=lambda x: (x[key_index], x[1]), reverse=True)

if __name__ == '__main__':
    # Hard-coded sample data representing lists of tuples where each tuple is (value_to_sort_by, original_index). 
    # We will test with a mix to demonstrate descending order.
    
    sample_data = [
        (30, 1),   # Value: 30, Index: 1 -> Should be first if sorted by value desc? Wait. Prompt says "sort ... based on the value at key_index". 
                   # If we define tuple as (value_for_sorting_key, original_id). Then sort_by_value means use index 0.
        (45, 3),   # Value: 45 -> Second place if equal? No, higher first. So this should be top.
        (12, 7),   # Value: 12
    ]

    # Let's create a scenario where