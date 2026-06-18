def sort_by_descending(numbers):
    """
    Sorts a list of numbers in descending order using Python's built-in sorted function.
    
    Args:
        numbers (list[float|int]): A list of numeric values.
        
    Returns:
        list[float|int]: A new list containing the same elements as input, 
                         but ordered from largest to smallest.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing; no user input required.
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    
    # Perform the sort operation on a copy of original data to avoid modifying reference
    sorted_data = sort_by_descending(sample_data)
    
    # Output result for verification (optional print statement as per module standard practice if no specific output requirement exists other than logic correctness)
    print("Sorted descending:", sorted_data)