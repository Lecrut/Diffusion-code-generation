def sort_volume_descending(volumes):
    """
    Sorts a list of volume measurements in descending order.
    
    Uses Python's built-in Timsort algorithm via the sorted() function with 
    reverse=True, which is highly optimized for real-world data (O(n log n) worst-case).

    Args:
        volumes (list): A list of numeric values representing volume measurements.

    Returns:
        list: New list containing the same elements in descending order.
    
    Note: This function does not modify the original list but returns a new sorted one.
    """
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample volume measurements
    volumes = [10.5, 23.7, 8.9, 45.6, 12.3, 67.8, 9.1]

    sorted_volumes = sort_volume_descending(volumes)

    # Output the result for verification
    print("Sorted volumes in descending order:")
    print(sorted_volumes)