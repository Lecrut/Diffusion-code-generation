def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order using Python's built-in 
    highly optimized Timsort algorithm via reverse=True.
    
    Args:
        numbers (list[int]): A list of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the same integers sorted in descending order.
    """
    # Using sort with key and reverse flag is efficient for standard integer lists.
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7, 3]
    result = sort_by_descending(sample_data)
    print(result)