def sort_by_descending(numbers):
    """
    Returns a new list containing the numbers from 'numbers' sorted in descending order.
    
    Uses Python's built-in Timsort algorithm via the `sorted` function, which is highly optimized for this task.
    
    Args:
        numbers (list of int/float): The input list of numerical values.
        
    Returns:
        list of int/float: A new list with elements in descending order.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [34, 78, 12, 90, -5]
    result = sort_by_descending(sample_data)
    print(result)