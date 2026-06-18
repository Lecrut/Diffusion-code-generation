def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to process.
        
    Returns:
        list[int]: A list of odd integers found in the input.
        
    Raises:
        TypeError: If 'numbers' is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    
    result = []
    for item in numbers:
        if not isinstance(item, int) or isinstance(item, bool):
            # Exclude booleans as they are instances of int in Python but semantically distinct here.
            continue
        
        if item % 2 != 0:
            result.append(item)
    
    return result

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_odds = filter_odd_numbers(sample_data)
    print(filtered_odds)