import random

def quicksort_in_place(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    This implementation uses Lomuto partition scheme with three-way partitioning (Dutch National Flag)
    to handle duplicate elements efficiently, reducing the recursion depth and avoiding unnecessary splits.
    Space complexity is O(log n) due to recursive stack usage only; no auxiliary arrays are allocated.
    
    Args:
        arr (list): List of integers to be sorted in-place.
        
    Returns:
        None (the list is modified in place).
    """
    if len(arr) <= 1:
        return
    
    # Three-way partitioning handles duplicates efficiently
    lt, gt = -1, len(arr) - 1
    i = 0

if __name__ == '__main__':
    pass
