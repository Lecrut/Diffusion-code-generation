from typing import List

def filter_negative_numbers(numbers: List[int]) -> List[int]:
    """
    Returns a new list containing only the negative integers from the input list.
    
    Optimized using list comprehension, which is implemented in C and generally faster 
    than explicit for-loops with append operations in Python.

    Args:
        numbers (List[int]): A list of integers to filter.

    Returns:
        List[int]: A new list containing only the negative integers from 'numbers'.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, CLI args, etc.)
    sample_data = [10, -5, 3, -2.5, -8, 0, -1]

    result = filter_negative_numbers(sample_data)

    print("Input:", sample_data)
    print("Negative numbers only:", result)