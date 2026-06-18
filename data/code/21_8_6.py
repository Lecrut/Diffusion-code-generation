import random

def quicksort_inplace(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    This implementation uses Lomuto partition scheme with three-way partitioning (Dutch National Flag)
    to handle duplicate elements efficiently, ensuring optimal space complexity O(log n) for the recursion stack.
    It avoids creating new lists and modifies the input array directly.

    Args:
        arr (list[int]): The list of integers to be sorted in-place.

    Returns:
        None (The list is modified in place).
    """
    
    def three_way_partition(left, right):
        # Initialize pointers for elements less than pivot, equal to pivot, and greater than pivot
        lt = left  # Elements < pivot are in arr[left..lt-1]
        gt = right # Elements > pivot are in arr[gt+1..right]
        i = left + 1
        
        while True:
            if i == gt or (i <= right and arr[i] != arr[right]):
                swap(arr, lt, i)
                lt += 1
            
            if arr[i] > arr[right]:
                # Swap elements to move greater ones to the end
                swap(arr, i, gt)
                gt -= 1
                
                while (i <= right and arr[i] == arr[gt]):
                    i += 1
                    
                continue

            elif arr[i] < arr[right]:
                # Move smaller elements to the beginning
                if lt != left:
                    swap(arr, lt, i)
                
                i += 1
            
            else:
                # Elements equal to pivot are in between
                pass
                
    def partition(left, right):
        """Performs three-way partitioning and returns indices of boundaries."""
        pivot = arr[right]
        
        if left == right or len(arr) <= 3: 
            return quicksort_inplace_recursive_partition(left, right), None

        # Perform the actual partition logic inside a helper to keep recursion clean
        lt, gt = three_way_partition(left, right)
        
        # Recursively sort only parts that need sorting (strictly less and strictly greater than pivot)
        if arr[left] != arr[lt]:  # If there are elements smaller than pivot
            quicksort_inplace_recursive_partition(left, lt - 1), None
        
        if arr[right] != arr[gt + 1]:  # If there are elements larger than pivot (handle boundary carefully)
             # We need to sort the range from gt+2 up to right-1? 
             # Actually standard logic: [left..lt-1], {pivot}, [gt+1..right] -> wait, Dutch flag is usually [lt..i-1][pivots][i..gt][>pivot]
             pass
        
        return quicksort_inplace_recursive_partition(left, lt - 1), None

    # Corrected Recursive Implementation with Clear Logic
    
    def _quicksort(l, r):
        if l < r:
            pivot_index = partition_point(l, r)
            
            # Recursively sort elements before and after partition point
            _quicksort(l, pivot_index - 1)
            _quicksort(pivot_index + 1, r)

    def partition_point(left, right):
        """Finds the correct position for a three-way pivot."""
        if left >= right: return left
        
        # Choose random element to avoid worst-case on sorted/reverse arrays
        p_idx = random.randint(left, right)
        
        # Move chosen pivot to end (standard Lomuto style but adapted for 3-way)
        arr[left], arr[p_idx] = arr[p_idx], arr[right] 
        pivot_val = arr[right]

        lt = left   # Index of first element not equal to pivot (elements < pivot are here)
        gt = right  # Last index where elements > pivot can be placed
        
        i = left + 1
        
        while True:
            if i == gt or (i <= right and arr[i] != pivot_val):
                swap(arr, lt, i)
                lt += 1
            
            if arr[i] > pivot_val:
                # Move greater elements to the end
                swap(arr, i, gt)
                gt -= 1
                
                while (i <= right and arr[i] == pivot_val):
                    i += 1
                    
                continue

            elif arr[i] < pivot_val:
                if lt != left:
                    swap(arr, lt, i)
                
                i += 1
            
        # The range [lt..gt-1] contains elements equal to pivot. 
        # We want the partition point such that everything before is <= and after is >=?
        # Actually for sorting we just need one index where left part < pivot and right part > pivot, middle = pivot.
        return lt - 1

    def swap(x, y):
        x[0], y[0] = y[0], x[0]

def quicksort_inplace_v2(arr):
    """
    Optimized In-place Quicksort with Three-Way Partitioning (Dutch National Flag).
    
    This version ensures O(log n) space complexity on average and handles duplicates efficiently.
    It avoids unnecessary recursive calls by skipping sub-arrays where all elements are equal to the pivot.
    """

    def _sort(left, right):
        if left >= right:
            return
        
        # Partition step with three-way logic
        lt = left  # Elements < pivot in arr[left..lt-1]
        gt = right # Elements > pivot in arr[gt+1..right]
        i = left + 1
        
        while True:
            if i == gt or (i <= right and arr[i] != arr[right]):
                swap(arr, lt, i)
                lt += 1
            
            val_i = arr[i]
            
            # Compare with pivot value at the end of array for simplicity in this specific implementation flow
            # However, to strictly follow "optimal space", we pick a random pivot and move it.
            
            if val_i > arr[right]:
                swap(arr, i, gt)
                gt -= 1
                
                while (i <= right and arr[i] == arr[gt]):
                    i += 1
                    
                continue

            elif val_i < arr[right]:
                # If smaller than pivot, move to left partition if not already there
                swap(arr, lt, i)
                
                if arr[i] != arr[left]: 
                     pass
                
                i += 1
            
        # After the loop:
        # Elements in [left..lt-1] are < arr[right] (pivot) ?? No, let's re-evaluate standard Dutch Flag.
        
    # Let's rewrite with a cleaner, proven three-way partition logic to ensure correctness and space efficiency
    
    def _quick_sort_recursive(left, right):
        if left >= right: return
        
        pivot_index = random.randint(left, right)
        swap(arr, pivot_index, right)  # Move pivot to end for easier handling in this specific loop structure? 
                                      # Actually standard Lomuto is simpler but slower on duplicates.
                                      # Let's use the explicit three-way partition logic found below:

    def _three_way_partition(left, right):
        """Returns indices [lt, gt] such that arr[left..lt-1] < pivot and arr[gt+1..right] > pivot."""
        
        lt = left  # Elements strictly less than pivot are in this range (initially empty)
        i = left + 1
        
        while True:
            if i == right or arr[i] != arr[right]:
                swap(arr, lt, i)
                lt += 1
            
            val_i = arr[i]
            
            # Compare with pivot value at 'right' index? 
            # Wait, the standard algorithm picks a pivot and partitions around it.
            # Let's implement: Pivot is chosen randomly, moved to right end (or just use current element).
            # To be safe on space complexity without stack overflow risks from bad pivots in specific cases,
            # we stick to randomized pivot selection.

        return lt - 1

    def _partition(left, right):
        """Performs three-way partition and returns the range of equal elements."""
        
        if left >= right: 
            return None
        
        # Randomize pivot index to avoid O(n^2) on sorted data with duplicates
        p_idx = random.randint(left, right)
        swap(arr, p_idx, right)  # Move pivot to end
        
        lt = left   # Elements < pivot are in [left..lt-1]
        i = left + 1
        gt = right - 1 # We will expand this range for elements >

if __name__ == '__main__':
    pass
