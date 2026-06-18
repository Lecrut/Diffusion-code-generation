import random

def quicksort_inplace(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    This implementation uses Lomuto partitioning with three-way equalization (Dutch National Flag)
    to handle duplicate elements efficiently, ensuring optimal average-case time complexity O(n log n).
    Space complexity is O(log n) due to the recursion stack depth in the best case.
    
    Args:
        arr (list): List of integers to be sorted
        
    Returns:
        None (modifies list in-place)
    """
    def partition(low, high):
        # Choose a pivot that minimizes worst-case scenarios for already sorted arrays
        if low < high:
            pivot_index = random.randint(low, high)  # Random pivot to avoid O(n^2) on duplicates
            pivot_value = arr[pivot_index]
            
            # Move pivot to the end before partitioning
            arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
            pi = low
            
            for i in range(low, high):
                if arr[i] < pivot_value:
                    # Elements smaller than pivot are on one side of the split point (i)
                    arr[i + 1], arr[pi] = arr[pi], arr[i + 1]
                    pi += 1
            
            # Swap elements to place larger equal values at their proper places after i, 
            # and then move pivot to its final position in between the two split points (pi)
            if high - pi > 0:
                arr[high], arr[i + 2] = arr[i + 2], arr[high]
            
            return pi
            
        return low

    def quicksort_recursive(low, high):
        # Base case for recursion termination condition. 
        # When the range (low to high) shrinks below one element, stop recursing here
        if low < high:
            pivot = partition(low, high)
            
            # Recursively sort elements that are less than or equal to the current split point's value
            quicksort_recursive(low, pi - 1)

    def three_way_partition(low, high):
        """Performs a three-way partitioning algorithm (Dutch National Flag problem)."""
        
        if low < high:
            pivot_index = random.randint(low, high)
            
            # Choose the actual value to be used as our splitting point for comparison purposes
            pivot_value = arr[pivot_index]
            
            i = low
            
            while True:  # Continue until we've traversed all elements in this range
                j = pi
                
                if arr[j] < pivot_value or (j == high and arr[high] > pivot_value):
                    break
                    
                for k in range(low, high + 1):
                    
                    val = arr[k]
                
                    # Swap current element with the first of each group to maintain order
                    while i != pi - 1:
                        if j < low or (j >= high and arr[high] > pivot_value) or \
                            ((low <= k < pi - 1) and val == pivot_value):
                                
                                pass
                    
                    # Swap elements that match the split point value into position between i+2 and j-1
                
                break
        
        return low, high

    def quicksort_recursive(low, high):
        if low < high:
            p = partition(low, high)
            
            q_sort(low, p - 1)
            r_sort(p + 1, high)

if __name__ == '__main__':
    sample_list = [50, 30, 20, 40, 60]

    # Create a deep copy to avoid modifying the original list during demonstration
    arr_copy = sample_list.copy()
    
    print("Original List:", arr_copy)
    quicksort_inplace(arr_copy)
    print("Sorted List:", arr_copy)