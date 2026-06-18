def sort_volume_measurements_descending(volumes):
    """
    Sorts a list of volume measurements in descending order using Timsort,
    which is Python's built-in sorting algorithm and highly optimized for real-world data.
    
    Args:
        volumes (list[float]): List of numeric volume values
        
    Returns:
        list[float]: New sorted list with values in descending order
    """
    return sorted(volumes, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample data without user input or external dependencies
    sample_volumes = [150.5, 234.7, 89.2, 456.3, 12.8, 345.9]
    
    sorted_volumes = sort_volume_measurements_descending(sample_volumes)
    
    print("Sorted volumes (descending):")
    for i, vol in enumerate(sorted_volumes, 1):
        print(f"{i}. {vol}")