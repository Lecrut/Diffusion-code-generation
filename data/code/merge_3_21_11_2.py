def sort_by_descending(numbers):
    """
    Sorts a list of numbers in descending order using Python's built-in sorted function.
    
    Args:
        numbers (list): A list of numerical values to be sorted.
        
    Returns:
        list: A new list containing the same elements as 'numbers' but sorted in descending order.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [34, 78, -52, 10, 99, 0.5, 23]
    
    sorted_result = sort_by_descending(sample_data)
    
    print("Original list:", sample_data)
    print("Sorted (descending):", sorted_result)