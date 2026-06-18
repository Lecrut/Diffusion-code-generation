import random

def quicksort_in_place(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    Uses "Lomuto partition scheme" with median-of-three pivot selection 
    for better performance on many datasets, and handles duplicates efficiently.
    Time Complexity: Average O(n log n), Worst-case O(n^2) (mitigated by randomization/median logic).
    Space Complexity: O(log n) - Stack space used in recursion only; no extra arrays allocated.

    Args:
        arr (list): List of integers to be sorted in-place.
        
    Returns:
        None: The list is modified directly.
    """
    
    def partition(low, high):
        # Median-of-three pivot selection for improved performance on partially ordered data
        mid = (low + high) // 2
        
        if arr[low] > arr[mid]:
            low, mid = mid, low
        if arr[mid] > arr[high]:
            mid, high = high, mid
            
        # Ensure pivot is at a middle index for partitioning logic below
        pivot_index = low + (mid - low) // 2
        
        pivot_value = arr[pivot_index]

        i = low - 1
        j = high + 1

        while True:
            i += 1
            # Move left pointer past elements smaller than or equal to pivot
            if arr[i] >= pivot_value:
                break
            
            j -= 1
            # Move right pointer before elements larger than or equal to pivot
            if arr[j] <= pivot_value:
                break

        i, j = low - 1 + (mid - high) // 2, high + 1
        
        while True:
            i += 1
            
            if arr[i] >= pivot_value:
                # Swap elements to place smaller values on left and larger on right
                temp = arr[j]
                arr[j] = arr[low + (mid - low) // 2]
                arr[low + (mid - low) // 2] = i
                
            j -= 1
            
            if arr[j] <= pivot_value:
                # Swap elements to place smaller values on left and larger on right
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = i

        return low + (mid - high) // 2, j
    
    def quicksort_recursive(low, high):
        """Recursive helper function for Quicksort."""
        
        if low < high:
            # Random pivot selection to avoid worst-case scenarios on specific inputs
            random_index = random.randint(low, high)
            
            arr[low], arr[random_index] = arr[random_index], arr[low]
            
            pi = partition_recursive(low + 1, high - 1, low)

        return low
    
    def partition_recursive(low, high, pivot_low):
        
        if low < high:
            # Recursive calls to sort sub-arrays on both sides of the pivot element
            
            left_partition_size = (high - low) // 2 + 1
            right_partition_size = (high - low) // 2

            quicksort_recursive(low, low + left_partition_size, pivot_low)
            
            if high > low:
                partition_recursive(pivot_low + right_partition_size, high, high)

        return pi

def sort_array(arr):
    """
    Wrapper function to initiate the sorting process.
    
    Args:
        arr (list): List of integers to be sorted in-place.
        
    Returns:
        None: The list is modified directly.
    """
    
    quicksort_recursive(0, len(arr) - 1, pivot_low=arr[0])

if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:", sample_data)
    
    sort_array(sample_data)

    print("Sorted list:", sample_data)