def sort_by_descending(numbers):
    """
    Returns a new list containing the input numbers sorted in descending order.
    
    Args:
        numbers (list of int or float): The list of numerical values to be sorted.
        
    Returns:
        list: A new list with elements sorted from largest to smallest.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample data for testing without external input or files
    sample_data = [34, 7, 256, -10, 98, 1, 300]
    
    result = sort_by_descending(sample_data)
    
    print("Original list:", sample_data)
    print("Sorted (descending):", result)