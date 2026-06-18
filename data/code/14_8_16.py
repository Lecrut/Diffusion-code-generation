def sort_volume_measurements_descending(volumes):
    """
    Sorts a list of volume measurements in descending order using Timsort,
    which is Python's built-in highly optimized sorting algorithm (O(n log n)).
    
    Args:
        volumes (list[float]): List of numeric volume values.
        
    Returns:
        list[float]: New sorted list with elements in descending order.
    """
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample data for testing without user input or external dependencies
    sample_volumes = [120.5, 45.3, 89.7, 230.1, 67.8, 12.4]
    
    sorted_volumes = sort_volume_measurements_descending(sample_volumes)
    
    print("Original volumes:", sample_volumes)
    print("Sorted (descending):", sorted_volumes)