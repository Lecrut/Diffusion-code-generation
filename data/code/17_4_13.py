import sys

def filter_even_numbers(numbers: list) -> list:
    """
    Returns a new list containing only the even numbers from the input list.
    Optimized by using a list comprehension, which is faster in CPython than an explicit loop due to internal optimizations and reduced interpreter overhead.
    
    Args:
        numbers (list): A list of integers.
        
    Returns:
        list: A new list containing only the even integers from 'numbers'.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    sample_data = [1, 4, 6, 8, -3, 0, 7, 9, 12]
    
    result = filter_even_numbers(sample_data)
    
    print("Original list:", sample_data)
    print("Filtered even numbers:", result)