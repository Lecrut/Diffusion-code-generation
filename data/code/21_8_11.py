import random

def quicksort_in_place(arr):
    """
    Sorts a list of integers in-place using an optimized Quicksort algorithm.
    
    This implementation uses Lomuto partition scheme with three-way partitioning 
    (Dutch National Flag) to handle duplicate elements efficiently, ensuring O(log n)
    stack space complexity and avoiding unnecessary recursive calls on equal partitions.
    
    Args:
        arr: List of integers to be sorted in-place
        
    Returns:
        None (modifies the list in place)
    """
    def three_way_partition(low, high):
        # Initialize pointers for elements less than pivot, between pivot and greater than pivot
        lt = low  # Elements < pivot end at index lt-1
        gt = high # Elements > pivot start at index gt+1
        i = low + 1
        
        while i <= gt:
            if arr[i] == arr[low]:
                i += 1
            elif arr[i] < arr[low]:
                arr[++lt], arr[i] = arr[i], arr[lt]
                i += 1
            else: # arr[i] > arr[low]
                arr[i], arr[--gt] = arr[gt], arr[i]
        
        return lt, gt

    def sort_recursive(low, high):
        if low < high:
            pivot_index_low, pivot_index_high = three_way_partition(low, high)
            
            # Recursively sort only the partitions that need sorting
            # Left partition (elements strictly less than pivot)
            if low <= pivot_index_low - 1:
                sort_recursive(low, pivot_index_low - 1)
                
                # Right partition (elements strictly greater than pivot)
                if pivot_index_high + 1 < high:
                    sort_recursive(pivot_index_high + 1, high)

    if len(arr) > 0:
        sort_recursive(0, len(arr) - 1)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        [34, 7, 23, 32, 5, 62],
        [],
        [1],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1],
        [5, 2, 8, 2, 5, 8]
    ]

    for i, test_input in enumerate(test_cases):
        # Create a copy to avoid modifying the original if needed later (though we modify copies)
        arr_copy = list(test_input)
        
        print(f"Test case {i + 1}:")
        print(f"Before: {arr_copy}")
        
        quicksort_in_place(arr_copy)
        
        print(f"After : {arr_copy}")
        assert arr_copy == sorted(arr_copy), f"Sorting failed for input {test_input}"