def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order using Timsort, 
    which is highly optimized for real-world data including partially sorted sequences.
    
    Args:
        numbers (list[int]): A list of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the same integers in descending order.
    """
    # Timsort's default behavior is ascending; reverse it for descending order efficiently.
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7, 3]
    result = sort_by_descending(sample_data)
    print(result)