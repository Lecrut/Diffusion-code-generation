def sort_pairs(pairs: list) -> list:
    """
    Sorts a list of (value, index) tuples based on the 'value' element in reverse order.

    Args:
        pairs (list): A list where each element is a tuple containing two elements: 
                     an integer value and its corresponding original index.

    Returns:
        list: A new list of tuples sorted by the first element (value) in descending order.

    Raises:
        TypeError: If input 'pairs' is not a list or if any element within pairs is not a tuple with exactly two elements.
    
    Complexity Analysis:
        Time Complexity: O(n log n), where n is the number of tuples, due to the sorting operation.
        Space Complexity: O(1) auxiliary (ignoring space required for output and recursion stack in Timsort).

    Example:
        >>> data = [(30, 2), (5, 0), (499, 6)]
        >>> sort_pairs(data)
        [(499, 6), (30, 2), (5, 0)]
    """
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")

    for item in pairs:
        if not isinstance(item, tuple) or len(item) != 2:
            raise TypeError(f"Each element must be a tuple of length 2. Got {item}.")

    return sorted(pairs, key=lambda x: x[0], reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_data = [(30, 2), (5, 0), (499, 6)]

    sorted_result = sort_pairs(sample_data)
    
    print("Original Data:")
    for val, idx in sample_data:
        print(f"({val}, {idx})")
        
    print("\nSorted Data (by value descending):")
    for val, idx in sorted_result:
        print(f"({val}, {idx})")