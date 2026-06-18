def sort_pairs(pairs: list) -> list:
    """
    Sorts a list of (value, index) tuples based on the 'value' element in reverse order.

    Args:
        pairs (list): A list where each element is a tuple containing two elements: 
                     an integer value and its corresponding original index.

    Returns:
        list: A new list of tuples sorted by the first element (value) in descending order.

    Complexity Analysis:
        Time Complexity: O(n log n), where n is the number of pairs, due to the sorting operation.
        Space Complexity: O(n), as a new list containing all elements is created during the sort.

    Example:
        >>> data = [(3, 0), (1, 2), (4, 1)]
        >>> result = sort_pairs(data)
        >>> print(result)
        [(4, 1), (3, 0), (1, 2)]
    """
    return sorted(pairs, key=lambda x: x[0], reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    sample_data = [(3, 0), (1, 2), (4, 1)]

    sorted_result = sort_pairs(sample_data)

    print("Original data:", sample_data)
    print("Sorted data:", sorted_result)