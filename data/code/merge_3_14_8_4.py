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
    # Hard-coded sample data representing various volume measurements
    sample_volumes = [150.5, 320.7, 89.2, 456.3, 12.8, 234.9]
    
    sorted_volumes = sort_volume_measurements_descending(sample_volumes)
    
    # Output the result to verify functionality without user input or external dependencies
    print("Sorted volumes (descending):")
    for vol in sorted_volumes:
        print(vol)