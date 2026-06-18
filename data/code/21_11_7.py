def sort_by_descending(numbers):
    """
    Returns a new list containing the input numbers sorted in descending order.
    
    Uses Python's built-in Timsort algorithm via the `sorted` function, which is highly optimized.
    
    Args:
        numbers (list of float or int): The list of numerical values to sort.
        
    Returns:
        list[float | int]: A new list with elements sorted from largest to smallest.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [3.14, 7, -2, 0, 99, 45.6, 1]
    
    sorted_result = sort_by_descending(sample_data)
    
    print("Original list:", sample_data)
    print("Sorted descending:", sorted_result)