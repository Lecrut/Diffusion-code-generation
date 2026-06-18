def sort_by_descending(numbers: list) -> list:
    """
    Sorts a list of integers in descending order efficiently.
    
    Args:
        numbers (list): A list of integers to be sorted.
        
    Returns:
        list: A new list containing the same integers, sorted from highest to lowest.
    """
    # Using Python's built-in sort is highly optimized and efficient for standard integer lists.
    # Sorting in-place then creating a copy ensures efficiency (O(n log n) time complexity).
    return [x for x in sorted(numbers, reverse=True)]

if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 98, 76, 43, 21]
    result = sort_by_descending(sample_data)
    print(result)