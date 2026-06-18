def sort_pairs(pairs: list) -> list:
    """
    Sorts a list of (value, index) tuples based on the 'value' element in reverse order.

    Args:
        pairs (list): A list where each element is a tuple containing two elements: 
                      an integer value and its corresponding original index.
    
    Returns:
        list: A new list containing the same tuples sorted by their first element (value) 
              in descending order. The original input list remains unchanged if it contains duplicates,
              as Python's sort is stable; however, since we are sorting a copy internally for return,
              this function does not modify the input in place to ensure safety unless explicitly requested.

    Raises:
        TypeError: If 'pairs' is not a list or if any element within 'pairs' is not a tuple of length 2.

    Complexity Analysis:
        Time Complexity: O(n log n), where n is the number of tuples in the input list, 
                         due to the sorting operation performed by Python's built-in sort (Timsort).
        Space Complexity: O(n) for storing the result and potentially during the sorting process.

    Example:
        >>> data = [(3, 0), (1, 2), (4, 5)]
        >>> sorted_data = sort_pairs(data)
        >>> print(sorted_data)
        [(4, 5), (3, 0), (1, 2)]
    """
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")

    for item in pairs:
        if not isinstance(item, tuple) or len(item) != 2:
            raise TypeError(f"Each element in the list must be a tuple of length 2. Got {item}.")

    # Create a copy to avoid modifying the original input and sort it by value descending
    return sorted(pairs, key=lambda x: x[0], reverse=True)

if __name__ == '__main__':
    sample_data = [(3, 10), (5, 2), (8, 7), (3, 4)]
    
    # Process the data using our function
    sorted_result = sort_pairs(sample_data)

    print("Original Data:", sample_data)
    print("\nSorted Data (by value descending):")
    for item in sorted_result:
        print(item)