def sort_by_descending(numbers):
    """
    Sorts a list of numbers in descending order using Python's built-in sorted function.
    
    Args:
        numbers (list): A list of numerical values to be sorted.
        
    Returns:
        list: A new list containing the same elements as input, but sorted in descending order.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 5, 9, 2, 6]
    result = sort_by_descending(sample_data)
    print(result)