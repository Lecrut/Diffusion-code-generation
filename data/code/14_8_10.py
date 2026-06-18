def sort_volume_measurements_descending(volumes):
    """
    Sorts a list of volume measurements in descending order.
    
    This function uses Python's built-in sorted() with reverse=True, which 
    leverages Timsort (a hybrid stable sorting algorithm). For general-purpose 
    lists like this one, Timsort is highly efficient because it performs well 
    on many kinds of data sequences and requires O(n log n) time complexity.
    
    Args:
        volumes (list[float|int]): List of volume measurements to sort.
        
    Returns:
        list: A new sorted list in descending order.
    """
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    sample_volumes = [100, 50, 23.5, 75.4, 98.6, 5]
    
    # Process the data using our optimized function
    sorted_volumes = sort_volume_measurements_descending(sample_volumes)
    
    print("Sorted volumes in descending order:", sorted_volumes)