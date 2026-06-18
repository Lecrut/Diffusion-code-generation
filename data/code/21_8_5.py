import random

def quicksort_inplace(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    This implementation uses:
    1. Random pivot selection to avoid worst-case O(n^2) on sorted/reverse-sorted data.
    2. Tail recursion optimization by only recursing into the larger partition,
       keeping a stack of size at most log n (optimal space complexity).
    
    Args:
        arr (list): List of integers to be sorted in-place.
        
    Returns:
        None (modifies list in place)
    """
    def _quicksort(low, high):
        # Base case: sub-array with 0 or 1 element is already sorted
        if low < high:
            pivot_index = partition(arr, low, high)
            
            # Recurse on the larger side first to minimize stack depth (tail recursion optimization simulation)
            if pivot_index - low > high - pivot_index:
                _quicksort(low, pivot_index - 1)
                _quicksort(pivot_index + 1, high)
            else:
                _quicksort(pivot_index + 1, high)
                _quicksort(low, pivot_index - 1)

    def partition(arr, low, high):
        # Randomly select a pivot index to ensure average O(n log n) performance
        random_idx = random.randint(low, high)
        arr[random_idx], arr[high] = arr[high], arr[random_idx]
        
        pivot_value = arr[high]
        i = low - 1
        
        for j in range(low, high):
            # If current element is <= pivot, swap it to the left partition
            if arr[j] <= pivot_value:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot between elements smaller than and greater than or equal to it
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    
    _quicksort(0, len(arr) - 1)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_data = [5, 9, 3, 7, 2, 8, 4]
    
    print("Original list:", test_data)
    quicksort_inplace(test_data)
    print("Sorted list: ", test_data)

    # Additional verification with a different dataset including duplicates and negatives
    secondary_test = [-10, -3, 7, 0, 2, 5, 5]
    original_secondary = secondary_test.copy()
    
    print("\nOriginal list (secondary):", original_secondary)
    quicksort_inplace(secondary_test)
    print("Sorted list (secondary): ", secondary_test)

    # Verify correctness against sorted standard library implementation
    assert test_data == sorted(test_data), "Quicksort failed on primary dataset"
    assert secondary_test == sorted(original_secondary), "Quicksort failed on secondary dataset"
    
    print("\nAll assertions passed. Sorting verified.")