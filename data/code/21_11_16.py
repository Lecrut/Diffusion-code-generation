def sort_by_descending(numbers):
    """
    Returns a new list containing the input numbers sorted in descending order.
    
    Args:
        numbers (list of float/int): The list of numerical values to be sorted.
        
    Returns:
        list of float/int: A new list with elements sorted from largest to smallest.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [3.5, 1.2, -4.7, 0, 8, 99]
    result = sort_by_descending(sample_data)
    print(result)