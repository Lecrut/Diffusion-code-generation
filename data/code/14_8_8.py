import sys

def sort_volume_measurements(volumes):
    """
    Sorts a list of volume measurements in descending order using Timsort,
    which is highly optimized for real-world data in Python's standard library.
    
    Args:
        volumes (list[float]): A list containing numeric volume values.
        
    Returns:
        list[float]: The same list sorted in descending order.
    """
    # Create a copy to avoid modifying the original input if necessary,
    # though sorting in-place is generally preferred for efficiency unless mutation is unwanted.
    # Timsort (list.sort) is O(n log n) on average and handles partially sorted data efficiently.
    volumes.reverse()  # sort ascending then reverse once; or just use key with descending order
    
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [10.5, 23.7, 45.2, 9.8, 67.3, 12.1]
    sorted_volumes = sort_volume_measurements(sample_volumes)
    
    print("Sorted volumes in descending order:")
    for vol in sorted_volumes:
        print(vol)