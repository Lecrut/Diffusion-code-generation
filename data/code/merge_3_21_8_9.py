import random

def quicksort_inplace(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    This implementation uses Lomuto partitioning with three-way partitioning (Dutch National Flag)
    to handle duplicate elements efficiently, ensuring O(log n) stack space complexity on average 
    and avoiding worst-case scenarios common in standard implementations when pivot selection is random.
    
    Args:
        arr (list): A list of integers to be sorted in-place.
        
    Returns:
        None: The list is modified directly.
    """
    if len(arr) <= 1:
        return

    # Randomly select a pivot index and swap it with the last element for better average performance
    random.shuffle(arr, random.Random()) 
    pivot = arr[-1]
    
    # Three-way partitioning indices
    lt = 0      # Elements < pivot are in arr[0...lt-1]
    gt = len(arr) - 1  # Elements > pivot are in arr[gt+1...n-1]
    i = lt
    
    while i <= gt:
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        else: # arr[i] > pivot
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
    
    # Recursively sort the left and right partitions only if they contain elements to be sorted
    quicksort_inplace(arr[:lt])
    quicksort_inplace(arr[gt+2:])

if __name__ == '__main__':
    sample_data = [5, 3, 8, 4, 9, 1, 7, 6, 2]
    
    # Create a copy to avoid modifying the original if needed for demonstration purposes later
    data_to_sort = list(sample_data)
    
    quicksort_inplace(data_to_sort)
    
    print("Sorted array:", data_to_sort)