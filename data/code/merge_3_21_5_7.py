import time

def sort_and_count(numbers):
    """
    Accepts a list of numbers and returns:
        1) A new list with elements sorted in ascending order.
        2) The total count of even numbers from the original input list.

    Time complexity for sorting is O(n log n). Counting evens is O(n).
    Overall time complexity is dominated by sorting: O(n log n).

    Args:
        numbers (list): List of numeric values to sort and analyze.

    Returns:
        tuple: A tuple containing the sorted list and the count of even numbers.
    """
    # Create a copy to avoid modifying the original input if that matters,
    # though typically in functional contexts we might just return new structures.
    # Sorting creates O(n) space for Timsort (Python's default).
    sorted_numbers = sorted(numbers)

    even_count = sum(1 for num in numbers if num % 2 == 0)

    return sorted_numbers, even_count

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used here.
    sample_data = [5, 3, 8, 12, -4, 0, 7, 9]

    start_time = time.time()
    result_sorted, result_even_count = sort_and_count(sample_data)
    end_time = time.time()

    print(f"Original list: {sample_data}")
    print(f"Sorted list (ascending): {result_sorted}")
    print(f"Count of even numbers in original list: {result_even_count}")
    # Optional timing info for demonstration, though not strictly required by task.
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

    assert result_sorted == sorted(sample_data), "Sorting logic failed."
    expected_evens_count = 4  # 8, 12, -4, 0 are even in the sample list.
    assert result_even_count == expected_evens_count, "Even count logic failed."