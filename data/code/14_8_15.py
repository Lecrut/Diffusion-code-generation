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
    # Hard-coded sample data without user input or external dependencies
    sample_volumes = [1250.5, 876.3, 4500.0, 125.9, 3200.7, 999.9]
    
    # Perform sorting and display result
    sorted_volumes = sort_volume_measurements_descending(sample_volumes)
    print("Sorted volumes (descending):")
    for vol in sorted_volumes:
        print(vol)