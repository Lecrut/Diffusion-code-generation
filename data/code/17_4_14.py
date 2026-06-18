def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    This function uses generator expression within list constructor for memory efficiency,
    avoiding the creation of an intermediate list during iteration. It assumes the 
    input is a list or iterable of integers.

    Args:
        numbers (list): A list of integers to filter.

    Returns:
        list: A new list containing only even integers from the original list.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_data = [1, 4, 3, 8, -2, 9, 6, 7, 0, 5]
    
    # Process the data and print result without user input or external dependencies
    even_numbers = filter_even_numbers(sample_data)
    print(f"Input: {sample_data}")
    print(f"Even numbers only: {even_numbers}")