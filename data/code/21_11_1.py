def sort_by_descending(numbers):
    """
    Sorts a list of numbers in descending order using Python's built-in sorted function.
    
    Args:
        numbers (list[float|int]): A list of numeric values to be sorted.
        
    Returns:
        list[numeric]: A new list containing the same elements as 'numbers' but sorted in descending order.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [35, 12, 89, -4, 0, 67]
    
    result = sort_by_descending(sample_data)
    
    print("Original list:", sample_data)
    print("Sorted (descending):", result)