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
    # Hard-coded sample data representing volume measurements
    volumes = [120.5, 89.3, 456.7, 23.1, 500.0, 12.5]
    
    sorted_volumes = sort_volume_measurements_descending(volumes)
    
    # Output the result for verification (no user input required)
    print("Sorted volumes in descending order:")
    for i, vol in enumerate(sorted_volumes):
        print(f"{i + 1}. {vol}")