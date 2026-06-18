import timeit

def filter_negative_numbers(numbers: list) -> list:
    """
    Returns a new list containing only the negative integers from the input list.
    Optimized using a generator expression within a constructor to avoid intermediate lists,
    which improves memory efficiency and execution speed for large inputs.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing only the negative integers from 'numbers'.
    """
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, network access, or file I/O is required.
    sample_data = [-5, -10, 3, -7, 20, -4, 89, -1]

    result = filter_negative_numbers(sample_data)

    print("Input:", sample_data)
    print("Negative numbers only:", result)

    # Optional performance benchmark for demonstration purposes.
    time_taken = timeit.timeit(
        stmt=f"filter_negative_numbers({sample_data!r})",
        setup="from __main__ import filter_negative_numbers",
        number=10000,
    )
    
    print(f"\nTime taken to process 10,000 iterations: {time_taken:.4f} seconds")