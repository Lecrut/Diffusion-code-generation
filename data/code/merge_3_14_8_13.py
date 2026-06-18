def sort_volume_measurements_descending(volumes):
    """
    Sorts a list of volume measurements in descending order using Timsort,
    which is Python's built-in sorting algorithm and highly optimized 
    for real-world data (including partially sorted sequences).
    
    Args:
        volumes (list[float]): List of numeric values representing volume measurements.
        
    Returns:
        list[float]: A new list with the same elements in descending order.
    """
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample data for testing without user input or external dependencies
    sample_volumes = [10.5, 23.7, 8.9, 45.2, 6.3, 30.1, 12.8]
    
    sorted_volumes = sort_volume_measurements_descending(sample_volumes)
    
    print("Sorted volumes (descending):")
    for vol in sorted_volumes:
        print(f"{vol}")