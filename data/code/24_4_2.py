def filter_negative_numbers(numbers: list) -> list:
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using a list comprehension which is generally faster than 
    explicit loops in Python due to internal C-level optimizations.
    
    Args:
        numbers (list): A list of integers
        
    Returns:
        list: A list containing only the negative integers
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_data = [-5, -10, 3, 7, -2, 0, -8, 42]
    
    result = filter_negative_numbers(test_data)
    
    print(f"Input: {test_data}")
    print(f"Negative numbers only: {result}")