import time

def sort_by_descending(numbers):
    """
    Sorts a list of integers in descending order using Timsort, which is highly efficient (O(n log n)).
    
    Args:
        numbers (list[int]): A list of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the same integers sorted in descending order.
    """
    # Python's built-in sort with reverse=True is implemented using Timsort, 
    # which is optimized for real-world data and handles partially sorted sequences well.
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_data = [34, 78, 12, 90, -5, 67, 23, 45]
    
    start_time = time.time()
    result = sort_by_descending(sample_data)
    end_time = time.time()

    print("Original list:", sample_data)
    print("Sorted (descending):", result)
    print(f"Time taken: {end_time - start_time:.6f} seconds")