def sort_by_descending(numbers):
    """
    Returns a new list containing the input numbers sorted in descending order.
    
    Args:
        numbers (list of float or int): The list of numerical values to be sorted.
        
    Returns:
        list of float or int: A new list with elements sorted from largest to smallest.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sample_data = [3.5, 10, -2, 7.8, 4, 9]
    
    result = sort_by_descending(sample_data)
    
    print("Original list:", sample_data)
    print("Sorted descending:", result)