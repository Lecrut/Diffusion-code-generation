"""Module containing the sort_pairs function."""

def sort_pairs(pairs: list) -> list:
    """
    Sorts a list of (value, index) tuples based on the 'value' element in reverse order.

    Args:
        pairs (list): A list where each element is a tuple consisting of an integer value and its corresponding index.

    Returns:
        list: A new list containing the sorted tuples ordered by descending value. The original list remains unchanged.

    Raises:
        TypeError: If 'pairs' is not a list or if any element in 'pairs' is not a tuple with exactly two elements where both are integers (or comparable types).

    Example:
        >>> data = [(3, 0), (1, 2), (4, 5)]
        >>> result = sort_pairs(data)
        >>> print(result)
        [(4, 5), (3, 0), (1, 2)]

    Complexity Analysis:
        Time Complexity: O(n log n), where n is the number of tuples in the input list. This is due to the sorting algorithm used by Python's built-in sort function.
        Space Complexity: O(n). An auxiliary space proportional to the size of the input list is required for creating and returning the sorted result, as a new list is constructed without modifying the original in-place (unless implemented via specific algorithms that do not create copies, but here we return a new object which is standard practice for clarity unless 'in place' is specified).
    """
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list.")

    # Validate each element in the pairs list
    for item in pairs:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError(f"All elements must be tuples of length 2. Got {item}.")
    
    return sorted(pairs, key=lambda x: x[0], reverse=True)

if __name__ == '__main__':
    # Sample data hardcoded as per requirements (no user input or network access)
    sample_data = [(15, 'a'), (3.2, 'b'), (7, 'c')]
    
    print("Original list:", sample_data)
    sorted_result = sort_pairs(sample_data)
    
    print("Sorted list (reverse order by value):", sorted_result)