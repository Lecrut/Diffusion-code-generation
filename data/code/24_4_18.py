def filter_negative_numbers(numbers: list) -> list:
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using a generator expression within list() to avoid creating an intermediate 
    full-size filtered list before returning, which is memory efficient and generally faster 
    for large datasets in Python due to reduced allocation overhead.

    Args:
        numbers (list): A list of integers.
        
    Returns:
        list: A new list containing only the negative integers from 'numbers'.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_data = [-5, -10, 3, 7, -2, 0, -8, 42]
    
    result = filter_negative_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Filtered negative numbers:", result)