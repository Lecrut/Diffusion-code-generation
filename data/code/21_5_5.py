import time

def sort_and_count(numbers):
    """
    Accepts a list of numbers and returns:
        1) A sorted copy in ascending order (ascending).
        2) The total count of even numbers from the original input.

    Optimized for O(n log n) sorting using Timsort (built-in sort), 
    with an O(n) pass to count evens.

    Parameters:
        numbers (list): List of integers or floats.

    Returns:
        tuple: (sorted_list, even_count)
    """
    # Create a copy to avoid modifying the original list before sorting
    sorted_numbers = numbers.copy()
    
    # Sort in ascending order using Python's efficient Timsort algorithm
    sorted_numbers.sort()
    
    # Count evens in one pass over the original (or sorted, result is same)
    even_count = sum(1 for num in numbers if num % 2 == 0)
    
    return sorted_numbers, even_count

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    sample_data = [5, -3, 8, 4, 12, 7, 9, 2]

    start_time = time.perf_counter()
    result_sorted, result_even_count = sort_and_count(sample_data)
    end_time = time.perf_counter()

    print("Original list:", sample_data)
    print("Sorted list (ascending):", result_sorted)
    print(f"Total count of even numbers: {result_even_count}")
    
    # Optional performance check for demonstration purposes only