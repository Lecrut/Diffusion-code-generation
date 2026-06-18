import random

def sort_volume_measurements_volumes(volume_list: list) -> list:
    """
    Sorts a list of volume measurements in descending order using Timsort,
    which is optimized for real-world data and available as the default 
    sorting algorithm in Python. It ensures O(n log n) average time complexity
    with high space efficiency.

    Args:
        volume_list (list): List of numeric values representing volume measurements.

    Returns:
        list: A new list containing the sorted volume measurements in descending order.
        
    Note:
        This function does not modify the original input list but returns a 
        freshly sorted version to maintain immutability for the caller where necessary.
    """
    # Create a copy of the input list to avoid side effects on the original data structure
    unsorted_volumes = volume_list.copy()

    # Sort in ascending order first, then reverse it to achieve descending order
    unsorted_volumes.sort(reverse=True)
    
    return unsorted_volumes

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes. 
    # No user input or external dependencies are required here.
    sample_measurements = [45, 120, 30, 89, 67, 23, 99]

    sorted_volumes = sort_volume_measurements_volumes(sample_measurements)
    
    print("Sorted volume measurements (descending order):")
    for vol in sorted_volumes:
        print(vol)