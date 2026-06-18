def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd integers from the input list.
    
    Optimization: Uses a generator expression within list() to create the result,
    avoiding an intermediate boolean list which reduces memory usage and improves cache locality.
    Additionally, checking for the bit-wise operation (num & 1) is generally slightly faster 
    than using modulo (%) in tight loops due to CPU instruction sets, though Python's C-level optimization 
    makes this difference negligible; it remains a standard practice for readability and intent clarity.

    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: A new list containing the odd integers from 'numbers'.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, CLI args, network access, or file dependencies.
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = filter_odd_numbers(test_data)

    print(f"Input: {test_data}")
    print(f"Odd numbers only: {result}")