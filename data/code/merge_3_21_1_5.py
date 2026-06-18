import random  # Only used to generate sample data for testing; no external interaction required.

def sort_by_descending(numbers: list) -> list:
    """
    Returns a new list containing integers from 'numbers' sorted in descending order.
    
    This function uses Python's built-in Timsort algorithm via the reverse=True parameter,
    which provides O(n log n) average time complexity and is highly optimized for real-world data.

    Args:
        numbers (list): A list of integers to be sorted.

    Returns:
        list: A new list with elements in descending order.
    
    Note: This function does not modify the original list but returns a copy.
    """
    # Using built-in sort is highly efficient due to Timsort optimization (O(n log n) average).
    # Sorting in-place and returning reversed or using key/reverse flag avoids extra memory overhead of slicing.
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing; no user input required.
    sample_data = [45, 12, -30, 89, 67, 1, -1]

    result = sort_by_descending(sample_data)
    
    print("Sorted list in descending order:")
    for num in result:
        print(num)