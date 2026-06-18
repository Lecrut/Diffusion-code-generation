def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order using Python's built-in Timsort,
    which is highly optimized (O(n log n) average time complexity).
    
    Args:
        numbers (list[int]): A list containing integer values.
        
    Returns:
        list[int]: A new list with the same elements sorted from largest to smallest.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [34, 789, -120, 56, 0]

    result = sort_by_descending(sample_data)

    print("Sorted list (descending):", result)