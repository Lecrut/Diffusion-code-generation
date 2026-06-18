import timeit

def filter_negative_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the negative integers from the input list.
    
    This implementation uses a generator expression passed to a constructor,
    which is generally faster than traditional for-loops in Python due to C-level optimization.
    
    Args:
        numbers (list[int]): A list of integers.
        
    Returns:
        list[int]: A new list containing only the negative integers from 'numbers'.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies.
    # These are random-looking integer lists that include both positive and negative numbers.
    sample_list_1 = [-5, 3, -2, 8, -9, 0, -7]
    sample_list_2 = [10, 42, -1, 6, 20, -100, 5, -3]

    print("Input List 1:", sample_list_1)
    result_set1 = filter_negative_numbers(sample_list_1)
    print(f"Output (Negative from Set 1): {result_set1}")

    print("\nInput List 2:", sample_list_2)
    result_set2 = filter_negative_numbers(sample_list_2)
    print(f"Output (Negative from Set 2): {result_set2}")

    # Optional: Simple benchmark to demonstrate performance characteristics.
    # This executes the function multiple times in a tight loop without external input.
    iterations = 10000
    elapsed = timeit.timeit(
        setup='nums=[-5,3,-2,8,-9,0,-7]', 
        stmt=f'filter_negative_numbers(nums)', 
        number=iterations
    )
    
    average_time_per_call = elapsed / iterations
    print(f"\nPerformance Test: {average_time_per_call:.4f} seconds per call on average for 10k runs.")