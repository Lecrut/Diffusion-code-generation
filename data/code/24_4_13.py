import timeit

def filter_negative_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using a list comprehension which is generally faster than 
    explicit for-loops in Python due to internal C-level optimizations.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: A new list containing only the negative integers from input.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    sample_data = [-5, -1, 3, -8, 0, -2, 7, -9]

    result = filter_negative_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Filtered Negative Numbers:", result)