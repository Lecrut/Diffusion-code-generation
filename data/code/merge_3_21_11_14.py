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
    sample_data = [3, 7, 1, 9, 4, 2]
    result = sort_by_descending(sample_data)
    print(result)