def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the even numbers from the input list.
    
    Optimized by using a generator expression within a built-in function,
    which is more memory-efficient and often faster than explicit loops in Python.

    Args:
        numbers (list[int]): A list of integers to filter.

    Returns:
        list[int]: A new list containing only the even integers from the input.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_data = [-5, -4, 1, 3, 8, 9, 16, 27]
    
    even_numbers = filter_even_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Even numbers only:", even_numbers)