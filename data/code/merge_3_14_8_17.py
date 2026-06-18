def sort_volume_measurements_descending(volumes):
    """
    Sorts a list of volume measurements in descending order using Timsort,
    which is Python's built-in highly optimized sorting algorithm. It performs 
    O(n log n) comparisons and swaps on average but degrades gracefully for 
    partially sorted data or when all elements are equal (O(n)).

    Args:
        volumes (list of float/int): List containing volume measurements.

    Returns:
        list: A new list with values sorted in descending order. The original 
             input list remains unchanged as Python's sort is stable but returns a modified version via indexing logic or slice assignment if needed; however, since we are returning the result directly after sorting a copy to ensure immutability of input unless specified otherwise, let us use slicing:
    """
    # Create a shallow copy to avoid modifying the original list unexpectedly
    sorted_volumes = volumes.copy()
    
    # Sort in ascending order first (default) and then reverse for descending
    sorted_volumes.sort(reverse=True)

    return sorted_vomes

if __name__ == '__main__':
    sample_data = [12.5, 80, 34.7, -5, 99.9, 10]
    
    # Compute result without user input or external dependencies
    ordered_measurements = sort_volume_measurements_descending(sample_data)

    print("Sorted Volume Measurements (Descending):")
    for i, vol in enumerate(ordered_measurements):
        print(f"{i + 1}. {vol:.2f}")