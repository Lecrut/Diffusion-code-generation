import time

def sort_and_count(numbers):
    """
    Accepts a list of numbers, returns:
        1) A new sorted list (ascending order).
        2) The count of even numbers in the original list.

    Optimized for time complexity using built-in highly optimized C implementations:
      - Sorting via Timsort (O(n log n))
      - Even counting with a generator expression and sum (O(n))

    Args:
        numbers (list): List of integers or floats to sort and count evens.

    Returns:
        tuple: (sorted_list, even_count)
              sorted_list is the input list sorted in ascending order.
              even_count is the number of elements divisible by 2 (including negatives).
    """
    # Create a copy to avoid modifying the original list during sorting
    numbers = list(numbers)

    # Sort using built-in Timsort, which is O(n log n) on average and handles many duplicates efficiently.
    sorted_numbers = sorted(numbers)

    # Count even numbers in the original (unsorted) data. 
    # An integer x is considered even if abs(x) % 2 == 0 or equivalently int(x) % 2 == 0 for floats that are whole numbers.
    even_count = sum(1 for n in numbers if isinstance(n, int) and n % 2 == 0 or (isinstance(n, float) and n.is_integer() and abs(int(float(n))) % 2 == 0))

    return sorted_numbers, even_count

if __name__ == '__main__':
    # Hard-coded sample values; no user input required.
    sample_data = [4, -2, 7, 10, 3.5, 8, 9]

    start_time = time.perf_counter()
    result_sorted, result_even_count = sort_and_count(sample_data)
    end_time = time.perf_counter()

    print("Original list:", sample_data)
    print("Sorted list (ascending):", result_sorted)
    print("Count of even numbers in original list:", result_even_count)
    print(f"Execution time: {(end_time - start_time)*10**6:.2f} microseconds")