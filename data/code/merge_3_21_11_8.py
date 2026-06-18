def sort_by_descending(numbers):
    """
    Returns a new list containing the input numbers sorted in descending order.
    
    Uses Python's built-in Timsort algorithm via the `sorted` function, 
    which is highly optimized for real-world data and provides O(n log n) time complexity.

    Args:
        numbers (list): A list of numerical values to be sorted.

    Returns:
        list: A new list with elements in descending order.
    
    Example:
        >>> sort_by_descending([3, 1, 4, 1, 5])
        [5, 4, 3, 1, 1]
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [64, 34, 25, 12, 98, -7, 0, 45]
    
    result = sort_by_descending(sample_data)
    
    print("Sorted list in descending order:")
    for item in result:
        print(item)