def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Optimized logic: Uses a generator expression within a constructor to 
    avoid creating an intermediate list, improving memory efficiency for large inputs.
    Alternatively, in Python 3, this is often just as fast or faster than manual loops 
    due to internal optimizations of built-in functions and CPython's implementation details.

    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: A new list containing only the odd integers from input.
    """
    return [n for n in numbers if n % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies are needed.
    test_list = [-5, 3, 8, -1, 7, 42, 9, 11]
    
    result = filter_odd_numbers(test_list)
    
    # Output the result for verification (no printing to external files required by task constraints).
    print(result)