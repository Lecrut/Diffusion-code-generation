import timeit

def sort_by_descending(numbers):
    """
    Accepts a list of integers and returns a new list sorted in descending order.
    
    Args:
        numbers (list[int]): List of integers to be sorted.
        
    Returns:
        list[int]: A new list containing the same integers, sorted from largest to smallest.
        
    Complexity Analysis:
        Time Complexity: O(n log n) due to sorting. Python's Timsort is highly optimized 
                         and efficient for real-world data (O(n), nearly linear).
        Space Complexity: O(n) as a new list is created; the original list remains unchanged.
    """
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    sample_data = [5, 23, -10, 78, 4, 9, 65, 0]
    
    start_time = timeit.default_timer()
    result = sort_by_descending(sample_data)
    end_time = timeit.default_timer()

    print("Original list:", sample_data)
    print("Sorted (descending):", result)
    execution_time_ms = round((end_time - start_time) * 1000, 4)
    print(f"Execution time: {execution_time_ms} ms")