def sort_volume_measurements_descending(volumes):
    """
    Sorts a list of volume measurements in descending order using Timsort,
    which is Python's built-in sorting algorithm and highly optimized for real-world data.
    
    Args:
        volumes (list[float]): List of numeric volume measurements
        
    Returns:
        list[float]: New sorted list with values in descending order
    
    Time Complexity: O(n log n) average/worst case
    Space Complexity: O(log n) auxiliary space due to Timsort's implementation details
    """
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_volumes = [15.2, 8.7, 30.4, 6.9, 22.1, 11.3, 35.6]
    
    sorted_volumes = sort_volume_measurements_descending(sample_volumes)
    
    print("Original volumes:", sample_volumes)
    print("Sorted (descending):", sorted_volumes)