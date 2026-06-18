def filter_even_numbers(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimizes iteration by using a simple loop with direct modulo operation,
    avoiding unnecessary function calls or complex data structures that would add overhead.
    
    Args:
        numbers (list[int]): A list of integers to filter.
        
    Returns:
        list[int]: A new list containing only the even integers from input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_data = [1, 4, 3, 8, 9, 16, 7, 24]
    result = filter_even_numbers(sample_data)
    print(result)