def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using a generator expression passed to list() which is generally 
    faster than explicit loops in Python due to internal C-level optimizations,
    unless the filtering condition involves complex logic requiring iteration overhead.
    For simple conditions like this (x < 0), direct comprehension or filtered loop
    are both highly optimized; we use a generator expression for memory efficiency
    and speed on large lists.

    Args:
        numbers (list of int): A list containing integer values.

    Returns:
        list of int: A new list with only the negative integers from input.
    
    Time Complexity: O(n) where n is the number of elements in 'numbers'.
    Space Complexity: O(k) where k is the count of negative numbers (output size).
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No input(), sys.stdin, or arguments used.
    sample_data = [-5, -1, 3, -2, 8, -9, 0, -7]
    
    result = filter_negative_numbers(sample_data)
    
    print(f"Input: {sample_data}")
    print(f"Negative elements only: {result}")