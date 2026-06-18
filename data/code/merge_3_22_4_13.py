def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Optimized by using a generator expression within a list constructor,
    which avoids creating intermediate lists and is memory efficient for large inputs.
    Integer comparison (n % 2 != 0) is used to check parity without division overhead 
    where possible in Python's optimized C implementation of modulo on small integers.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: A new list containing only the odd integers from the input.
    """
    return [n for n in numbers if n % 2 != 0]

if __name__ == '__main__':
    sample_data = [-5, 3, -1, 8, 7, 0, 9, 4, 11, -6]
    
    # Process the data using our optimized function
    result = filter_odd_numbers(sample_data)

    print("Original list:", sample_data)
    print("Filtered odd numbers:", result)