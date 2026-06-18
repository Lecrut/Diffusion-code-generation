def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using a generator expression passed to list() which is memory efficient 
    and faster than explicit loops in Python due to C-level implementation details.
    
    Args:
        numbers (list[int]): A list of integers
        
    Returns:
        list[int]: A new list containing only the negative integers from input
        
    Raises:
        TypeError: If input is not a list or contains non-integer elements
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    for num in numbers:
        if not isinstance(num, int) or isinstance(num, bool):
            raise TypeError(f"All elements must be integers. Got {type(num).__name__}")

    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    sample_data = [-5, -1, 3, -7, 0, -2, 4, -9]
    
    result = filter_negative_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Negative numbers only:", result)