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
    sample_volumes = [120.5, 45.3, 89.7, 200.0, 67.8, 12.1]

    sorted_volumes = sort_volume_measurements_descending(sample_volumes)

    print("Sorted volumes (descending):")
    for vol in sorted_volumes:
        print(vol)