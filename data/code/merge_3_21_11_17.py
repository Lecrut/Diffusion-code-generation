def sort_by_descending(numbers):
    """
    Returns a new list of numbers sorted in descending order.
    
    Args:
        numbers (list[float|int]): A list of numeric values to be sorted.
        
    Returns:
        list[int|float]: A new list containing the same elements as 'numbers' 
                         but sorted from largest to smallest.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [34, 78, 12, 90, -5, 67]
    result = sort_by_descending(sample_data)
    print(result)