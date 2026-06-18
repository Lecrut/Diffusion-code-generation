"""
Module containing utilities to sort pairs of (value, index) based on value in reverse order.
"""

def sort_pairs(pairs: list[tuple]) -> list[tuple]:
    """
    Sorts a list of tuples where each tuple contains (value, index).
    
    The sorting is performed primarily by the 'value' element in descending (reverse) order.
    If two values are equal, their original relative order remains unchanged 
    (stable sort), as Python's default Timsort algorithm guarantees stability.

    Args:
        pairs (list[tuple]): A list of tuples where each tuple has exactly two elements:
            - The first element is the numeric value to be used for sorting.
            - The second element is an index associated with that value.

    Returns:
        list[tuple]: A new list containing the same number of tuples, sorted by 'value' in reverse order.
                     The original list is not modified.

    Raises:
        TypeError: If 'pairs' is not a list or if any element within 'pairs' is not a tuple with two elements.
    
    Complexity Analysis:
        Time Complexity: O(n log n), where n is the number of tuples in the input list, 
                         due to the sorting operation. Python's Timsort has this worst-case and average complexity.
        Space Complexity: O(n) for storing the output list and the temporary space required during sort operations.

    Example:
        >>> data = [(5, 10), (3, 2), (8, 4), (7, 6)]
        >>> result = sort_pairs(data)
        >>> result
        [(8, 4), (7, 6), (5, 10), (3, 2)]

    Note: This function creates and returns a new list; it does not modify the input list in-place.
    """
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")
    
    for i, pair in enumerate(pairs):
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError(f"Element at index {i} is not a valid (value, index) tuple. Expected two elements.")

    # The default Python sort uses Timsort which is stable and sorts in ascending order by default.
    # To achieve reverse order on the 'value' without creating key objects or using lambdas that slow it down significantly,
    # we can pass a custom key if needed, but simple unpacking with negation for numbers works well too.
    # However, to keep logic robust against non-numeric values causing negative issues (though type hint implies numeric context usually),
    # standard reverse sorting via the 'reverse=True' flag on items accessed by index is safer and clear.
    
    return sorted(pairs, key=lambda x: x[0], reverse=True)

if __name__ == '__main__':
    sample_data = [(15, 3), (42, 7), (8, 1), (15, 2), (99, 4)]
    
    # Sort the data and print results to demonstrate functionality without input prompts or external dependencies.
    sorted_result = sort_pairs(sample_data)
    print("Sorted pairs by value in reverse order:")
    for item in sorted_result:
        print(item)