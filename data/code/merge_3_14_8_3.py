def sort_volume_measurements_descending(volumes):
    """
    Sorts a list of volume measurements in descending order using Timsort,
    which is Python's built-in highly optimized sorting algorithm (O(n log n)).
    
    Args:
        volumes (list[float]): List of numeric volume values.
        
    Returns:
        list[float]: New sorted list with elements from largest to smallest.
    """
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [150.5, 32.8, 497.2, 12.1, 650.0, 89.4]
    sorted_volumes = sort_volume_measurements_descending(sample_volumes)
    
    print("Sorted volumes (descending):")
    for val in sorted_volumes:
        print(val)