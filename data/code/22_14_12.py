import statistics

def filter_odd_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the odd integers from the input list.
    
    Args:
        numbers (list[int]): A list of integers to process.
        
    Returns:
        list[int]: A new list with all odd numbers removed if none exist, 
                   or filtered down for odd numbers otherwise.

    Example:
        >>> filter_odd_numbers([1, 2, 3, 4])
        [1, 3]
        >>> filter_odd_numbers([])
        []
        >>> filter_odd_numbers([-5, -2, -7])
        [-5, -7]
    
    Note: This implementation uses a list comprehension for efficiency 
          and handles empty inputs or lists with no odd numbers gracefully.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_input = [1, -45, 6789, 34, -2, 'odd', None, True, False, 1.5, 3]

    result = filter_odd_numbers(sample_input)
    
    print(f"Input: {sample_input}")
    print("Filtered Odd Numbers:", result)