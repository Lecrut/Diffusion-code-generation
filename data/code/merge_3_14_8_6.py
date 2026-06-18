def sort_volumes_descending(volume_list):
    """
    Sorts a list of volume measurements in descending order using Python's 
    built-in Timsort, which is highly optimized and adaptive O(n log n).
    
    Parameters:
        volume_list (list[float | int]): List of numeric values representing volumes.
        
    Returns:
        list[float | int]: New sorted list with elements from largest to smallest.
    """
    return sorted(volume_list, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample volume measurements
    samples = [1250, 890, 3400, 670, 2100, 150]
    
    sorted_volumes = sort_volumes_descending(samples)
    
    print("Sorted volumes (descending):")
    for vol in sorted_volumes:
        print(vol)