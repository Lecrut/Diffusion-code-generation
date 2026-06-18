import time

def sort_and_count(numbers: list) -> tuple:
    """
    Accepts a list of numbers, returns a tuple with (sorted_list, even_number_count).
    
    Uses Timsort which has O(n log n) average and worst-case time complexity.
    Counts evens in one pass over the original list before sorting to ensure 
    stability if duplicate values exist during sort logic.

    :param numbers: List of numeric integers or floats (integers handled by even check).
    :return: Tuple containing sorted ascending list and count of even numbers from input.
    """
    # Count evens in the original list first to avoid needing a second pass after sorting,
    # though technically we could do it later; doing it early is semantically clearer for "original".
    even_count = sum(1 for n in numbers if isinstance(n, (int, float)) and n % 2 == 0)

    sorted_list = sorted(numbers)

    return sorted_list, even_count

if __name__ == '__main__':
    sample_data = [5, 3, -2, 8, 1.6, -4, 7]
    
    start_time = time.perf_counter()
    result_sorted, result_even = sort_and_count(sample_data)
    end_time = time.perf_counter()

    print("Original:", sample_data)
    print("Sorted:", result_sorted)
    print(f"Count of even numbers: {result_even}")
    
    # Optional performance note (commented out for strict output compliance if needed elsewhere)
    # execution_duration_ms = round((end_time - start_time) * 1000, 6)