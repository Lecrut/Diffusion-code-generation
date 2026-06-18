def filter_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    
    Optimized by using a generator expression within a list constructor,
    which avoids creating intermediate lists and minimizes memory usage.
    This approach is both time-efficient (single pass) and space-efficient.

    Args:
        numbers (list): A list of integers to filter.

    Returns:
        list: A new list containing only the odd integers from the input.
    """
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_data = [-5, 3, -1, 8, 7, 0, 9, 4, 6, 21]

    result = filter_odd_numbers(sample_data)

    print("Original list:", sample_data)
    print("Filtered odd numbers:", result)