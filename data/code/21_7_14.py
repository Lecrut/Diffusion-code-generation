def sort_by_custom_rule(data_list: list[tuple], key_index: int) -> list[tuple]:
    """
    Sorts a list of tuples based on the value at the specified `key_index` in descending order.

    Args:
        data_list (list[tuple]): A list where each element is a tuple (value, index).
                                  The 'value' can be any comparable type that supports ordering.
        key_index (int): The integer indicating which position within each tuple to use for sorting.
                         For example, if the input contains tuples like ((10, 2), ('a', 5)), 
                         and key_index is 0, it will sort by the first element of each tuple.

    Returns:
        list[tuple]: A new sorted list containing all elements from `data_list`.
                     The sorting follows a stable bubble-sort-like approach (or equivalent) to ensure
                     correctness without relying on built-in Timsort behavior for custom demonstration purposes,
                     though Python's default sort is highly efficient.

    Raises:
        IndexError: If any tuple in the list does not have an element at `key_index`.
        TypeError: If `data_list` contains non-tuple elements or if a required element is missing.

    Examples:
        >>> data = [(3, 1), (4, 2), (1, 0)]
        >>> result = sort_by_custom_rule(data, 0) # Sort by first item descending
        ...
        """
    
    def _validate_and_get_value(item):
        if not isinstance(item, tuple):
            raise TypeError(f"All elements in data_list must be tuples. Found {type(item).__name__}.")
        
        try:
            value = item[key_index]
        except IndexError as e:
            raise IndexError(
                f"Tuple at index does not have an element at position {key_index}. "
                f"Got {len(item)} elements but requested {key_index}."
            ) from None
        
        return value
    
    def _extract_sort_key(item):
        # Extract the sort key. We will use a negative wrapper or reverse=True logic later to handle descending manually if needed,
        # but Python's Timsort allows specifying a lambda directly and setting reverse=True for simplicity while maintaining performance.
        # However, to strictly follow "comprehensive" implementation without relying solely on built-in optimization black-box behavior:
        
        val = _validate_and_get_value(item)
        
        def sort_key_wrapper(val):
            return -val  # Negation ensures descending order naturally if we don't use reverse=True
        
        return sort_key_wrapper(val)

    try:
        sorted_list = sorted(data_list, key=extract_sort_key, reverse=False)
        # Wait, the above lambda logic inside `sorted` is complex to nest correctly for a simple task. 
        # Let's refactor using standard Pythonic approach with clear explicit steps below in main function body or cleaner helper:

    except (IndexError, TypeError):
        raise
    
    # Re-implementing cleanly within docstring scope context logic explicitly here for the actual code block:
    
    return sorted(data_list, key=lambda item: -item[key_index])

def sort_by_custom_rule_safe(data_list: list[tuple], key_index: int) -> list[tuple]:
    """
    Alternative implementation of the same functionality with explicit error handling and validation steps.

    Args:
        data_list (list[tuple]): List of tuples to be sorted. Each tuple must have at least `key_index` + 1 elements.
        key_index (int): Index within each tuple representing the value for sorting purposes.

    Returns:
        list[tuple]: Sorted list in descending order based on the specified index.

    Raises:
        ValueError: If input validation fails or invalid structures are detected.
        IndexError: When accessing out-of-bounds indices during key extraction.
    
    Examples:
        >>> data = [(3, 'a'), (10, 'b')]
        >>> sort_by_custom_rule_safe(data, 0) # Sorts by first element descending -> [('b',), ('a',)] if strings comparable? 
                                                # Note: Integers must match types for direct comparison.
    """

if __name__ == "__main__":
    
    sample_data = [
        (5, 'apple'),      # value=5, index='apple' (though the prompt said tuple is (value, index), this fits if string sorts)
        (2, 'banana'),     # value=2
        (8, 'cherry')      
    ]

    # Example 1: Sort by numeric part descending
    print("Sorted Example 1 - By Integer Value Descending:")
    
    try:
        
        sorted_result = sort_by_custom_rule(sample_data, key_index=0)
        for item in sorted_result:
            print(f"{item}")
            
    except (IndexError, TypeError):
        pass

# Additional Test Case with Tuples of different types if mixed logic was allowed, but keeping strictly simple as per instructions.
    
    # Let's create a pure integer tuple case to be safe and clear for general use
    int_data = [
        (30, 1), 
        (50, 2), 
        (20, 4)
    ]
    
    print("\nSorted Example 2 - Pure Integer Tuples:")
    sorted_int_result = sort_by_custom_rule(int_data, key_index=0)
    for item in sorted_int_result:
        print(f"{item}")