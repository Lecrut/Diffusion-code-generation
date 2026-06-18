import random

def quicksort_in_place(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    This implementation uses the "three-way partitioning" (Dutch National Flag) strategy
    to handle duplicate elements efficiently, ensuring O(log n) stack space on average 
    and avoiding unnecessary recursion for equal keys. It also employs random pivot selection
    to prevent worst-case scenarios with sorted or nearly-sorted inputs.

    Args:
        arr (list[int]): The list of integers to sort in-place.
        
    Returns:
        None (modifies the input list directly)
    """
    
    def partition_three_way(low, high):
        # Randomize pivot index to avoid worst-case performance on sorted data
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end
        
        lt = low      # Elements < pivot are in [low, lt-1]
        gt = high     # Elements > pivot are in [gt+1, high]
        
        i = low + 1   # Current element being examined; elements <= pivot are in [lt, i-1]

        while i <= gt:
            if arr[i] < arr[high]:
                # Swap with left boundary of non-pivot region
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > arr[high]:
                # Move right boundary inward, swap current to end (gt)
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
                # Do not increment i here; re-examine the element that swapped into position i
            else:
                # Equal pivot, just move forward
                i += 1
        
        return lt - 1, gt

    def sort_recursive(low, high):
        if low < high:
            l_idx, g_idx = partition_three_way(low, high)
            
            # Recursively sort the left part (elements strictly less than pivot)
            sort_recursive(low, l_idx - 1)
            
            # The middle section [l_idx+1 to gt-1] contains elements equal to pivot; no need to recurse
            
            # Recursively sort the right part (elements strictly greater than pivot)
            if g_idx > low: 
                sort_recursive(g_idx + 1, high)

    if not arr or len(arr) == 0:
        return
    
    sort_recursive(0, len(arr) - 1)

if __name__ == '__main__':
    # Hard-coded sample values including duplicates and unsorted data
    sample_data = [3, 6, 8, 10, 1, 2, 1, 3, 4, 5]
    
    print("Original list:", sample_data)
    
    quicksort_in_place(sample_data)
    
    print("Sorted list: ", sample_data)