def sort_pairs(pairs):
    """
    Sorts a list of (value, index) tuples based on the 'value' element in reverse order.

    This function takes an iterable of two-element tuples and returns a new sorted list.
    The sorting criteria is primarily determined by the first element of each tuple (the value).
    Tuples with equal values maintain their original relative order from the input list, as Python's
    stable sort preserves this characteristic.

    Parameters:
        pairs (list[tuple]): A list where each item is a tuple containing two elements: 
                             an integer 'value' and its corresponding index or identifier.

    Returns:
        list[tuple]: A new list of tuples sorted by the first element in descending order.

    Complexity Analysis:
        Time Complexity: O(n log n), where n is the number of pairs. This arises from the 
                        sorting algorithm used internally (typically Timsort).
        Space Complexity: O(n) for storing the result and any auxiliary data structures created during sort.

    Example:
        >>> input_data = [(3, 10), (5, 2), (3, 8)]
        >>> output = sort_pairs(input_data)
        >>> print(output)
        [(5, 2), (3, 10), (3, 8)]
    """
    return sorted(pairs, key=lambda x: x[0], reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files.
    sample_data = [(42, 'b'), (7, 'a'), (-5, 'c'), (100, 'd')]

    sorted_result = sort_pairs(sample_data)

    print("Original list:")
    for item in sample_data:
        print(item)

    print("\nSorted list (by value descending):")
    for item in sorted_result:
        print(item)