def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order using Timsort, 
    which is highly optimized for real-world data including partially sorted sequences.
    
    Args:
        numbers (list[int]): A list of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the same integers sorted in descending order.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [34, 789, -123, 56, 0, 1234]
    
    sorted_result = sort_by_descending(sample_data)
    
    print("Original list:", sample_data)
    print("Sorted in descending order:", sorted_result)