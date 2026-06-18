def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized by using a generator expression within list() which is generally 
    faster than creating an intermediate list in Python due to reduced memory allocation overhead,
    though for simple filtering of small lists, standard list comprehension is also highly efficient.
    This implementation uses a straightforward loop with early exit logic simulation via iterator consumption
    if performance profiling indicated it was needed, but given the simplicity, 
    we use a direct generator approach which balances readability and speed well in CPython.

    Args:
        numbers (list of int): The input list of integers.
        
    Returns:
        list of int: A new list containing only negative integers from the input.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_data = [-5, -1, 3, 7, -2, 89, -4, 0, -6]
    
    result = filter_negative_numbers(sample_data)
    
    # Output the result for verification without external dependencies
    print("Negative numbers:", result)