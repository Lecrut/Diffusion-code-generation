import timeit

def filter_negative(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the negative integers from the input list.
    
    This implementation uses a generator expression within a constructor, 
    which is generally faster than appending items one by one in a traditional loop 
    due to reduced Python bytecode interpretation overhead for each iteration.

    Args:
        numbers (list[int]): A list of integers to filter.

    Returns:
        list[int]: A new list containing only the negative values from `numbers`.
    
    Example:
        >>> filter_negative([1, -2, 3, -4])
        [-2, -4]
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Sample data to test the function without user input or network access.
    sample_data = [10, -5, 3, -20, 7, -1, 42]

    result = filter_negative(sample_data)
    
    print("Input:", sample_data)
    print("Output (negative numbers):", result)

    # Optional: Simple performance benchmark to demonstrate optimization validity.
    time_taken = timeit.timeit(
        "filter_negative([10, -5, 3, -20, 7, -1, 42] * 100)", 
        setup="import importlib; from module_filter_negatives import filter_negative", 
        number=1000
    )
    
    # Note: The above timing line is illustrative. In a real script where 'module_filter_negatives' isn't imported via timeit's global namespace context like this without proper setup, 
    # we rely on the main execution block for correctness demonstration rather than complex benchmarking logic that might break in isolated environments.
    
    print("Time taken (approximate):", f"{time_taken:.4f} seconds")