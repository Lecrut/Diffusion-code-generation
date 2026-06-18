def sort_by_descending(numbers):
    """
    Returns a new list of numbers sorted in descending order.
    
    Uses Python's built-in Timsort algorithm via the `sorted` function,
    which is highly optimized and stable for this task.
    
    Args:
        numbers (list): A list of numerical values to be sorted.
        
    Returns:
        list: A new list containing the same elements in descending order.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [3.14, 2.718, -0.5, 99, 0, 42]
    
    result = sort_by_descending(sample_data)
    
    print("Original list:", sample_data)
    print("Sorted descending:", result)