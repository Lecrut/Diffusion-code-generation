def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order using Python's built-in Timsort,
    which is highly optimized (O(n log n) average and worst-case time complexity).
    
    Args:
        numbers (list[int]): A list of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the same integers in descending order.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    sample_data = [34, 78, 91, -50, 23, 67, 12, 45, 89, 3]
    
    result = sort_by_descending(sample_data)
    
    # Output the sorted list to verify correctness (no interactive prompts used)
    print(result)