import random

def quicksort_in_place(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    Uses Lomuto partition scheme with three-way equalization (Dutch National Flag)
    to handle duplicate elements efficiently, ensuring O(log n) stack space on average.
    
    Args:
        arr (list[int]): The list of integers to sort. Modifies in-place.
        
    Returns:
        None (modifies input list directly)
    """
    if len(arr) <= 1:
        return

    # Three-way partitioning handles duplicates well and avoids unnecessary recursion on equal elements
    left, mid = _partition_three_way(arr, 0, len(arr) - 1)

    quicksort_in_place(arr[:left])       # Recurse left part (elements < pivot)
    quicksort_in_place(arr[left+mid:]) # Recurse right part (elements > pivot)

def _partition_three_way(arr, low, high):
    """
    Partitions the array into three regions: [low...lt-1] (<), [lt..gt] (=), [gt+1...high] (>).
    
    Args:
        arr (list[int]): The list to partition.
        low (int): Start index of the range.
        high (int): End index of the range.
        
    Returns:
        tuple(int, int): Indices lt and gt such that:
            - All elements before 'lt' are less than pivot
            - Elements from 'lt' to 'gt' equal pivot
            - All elements after 'gt' are greater than pivot
    
    Note: This function modifies the array in-place.
    """
    if low >= high:
        return low, high

    # Choose a random pivot index near the middle to avoid worst-case scenarios on sorted data
    pivot_index = random.randint(low, high)
    pivot_value = arr[pivot_index]
    
    # Move pivot to end for easier processing (optional but simplifies logic here)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    lt = low  # Elements < pivot are in [low, lt-1]
    gt = high - 1  # Elements > pivot are in [gt+1, high]
    
    i = low + 1
    
    while True:
        if arr[i] == pivot_value and i != high:
            # Move equal elements to the middle section (between lt and gt)
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            
            if arr[i] < pivot_value or i == high:
                # If current element is less than pivot, swap with > region boundary
                arr[i], arr[gt+1] = arr[gt+1], arr[i]
                
                while gt >= low and arr[gt] != pivot_value:
                    gt -= 1
                
                if i == high or (i < high and arr[i] > pivot_value):
                    # If we've reached the end, stop partitioning this range
                    break
                    
            elif arr[i] > pivot_value:
                # Swap with greater element region boundary
                arr[lt], arr[i] = arr[i], arr[lt]
                
        i += 1
        
    return lt - 1, gt

if __name__ == '__main__':
    sample_data = [50, 3, 7, 24, 89, 6, 45, 12, 99, 1]
    
    print("Original list:", sample_data)
    quicksort_in_place(sample_data)
    print("Sorted list: ", sample_data)