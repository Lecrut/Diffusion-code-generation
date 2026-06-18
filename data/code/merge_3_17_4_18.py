def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimization note: Iterates once through the list with direct comparison,
    avoiding unnecessary function calls or intermediate structures where possible.
    
    Args:
        numbers (list[int]): A list of integers to filter.
        
    Returns:
        list[int]: A new list containing only even integers from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_data = [1, 4, 3, 8, 5, 16, 9, 22]
    result_even_numbers = filter_even_numbers(sample_data)
    
    # Print the filtered list to verify output without user input or file access
    print(result_even_numbers)