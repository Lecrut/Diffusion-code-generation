def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order using Timsort, 
    which is highly optimized for real-world data (including partially sorted sequences).
    
    Args:
        numbers (list[int]): List of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the same integers in descending order.
    """
    # Python's built-in sort uses Timsort, which is O(n log n) on average 
    # and highly efficient for most datasets. We use reverse=True for descending order.
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 98, 76, 43, 10]
    result = sort_by_descending(sample_data)
    print(result)