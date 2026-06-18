import timeit

def filter_negative_numbers(numbers):
    """
    Returns a new list containing only the negative elements from the input list.
    
    Optimized using a list comprehension which is generally faster than explicit loops
    in Python due to internal optimizations and reduced bytecode interpretation overhead.
    Assumes the input is already an iterable of integers, so no type checking or conversion 
    logic (which would be slower) is performed at runtime for each element during filtering.

    :param numbers: List[int] - The list of integers to filter.
    :return: List[int] - A new list containing only negative integers.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, CLI args, or files)
    sample_data = [-5, -1, 3, 7, -2, -89, 42, -10]

    result = filter_negative_numbers(sample_data)
    
    print("Input:", sample_data)
    print("Filtered negative numbers:", result)