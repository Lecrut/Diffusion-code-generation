def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimization: Uses a generator expression within a list constructor to avoid
    creating an intermediate list during iteration, improving memory efficiency
    for large inputs while maintaining readability and performance.

    Args:
        numbers (list): A list of integers.
        
    Returns:
        list: A new list containing only the even integers from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_input = [1, 4, 6, 8, -2, 9, 35, 42]
    result = filter_even_numbers(sample_input)
    print(result)