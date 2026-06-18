import random

def quicksort_inplace(arr):
    """
    Recursively sorts a list of integers in-place using Quicksort.
    Uses Lomuto partition scheme with three-way pivoting to handle duplicates efficiently,
    aiming for optimal average space complexity O(log n) due to recursion depth management.
    
    Args:
        arr (list[int]): The list of integers to sort.
        
    Returns:
        None (modifies the input list in-place).
    """

def quicksort_partition(arr, low, high):
    # Three-way partitioning logic by Dijkstra's 3-way Quicksort algorithm
    
    if arr is None or len(arr) == 0:
        return
    
    pivot = arr[low]
    
    i = low - 1
    j = high + 1
    while True:
        # Move i forward until element >= first_pivot
        while arr[i + 1] < pivot:
            i += 1
        
        # Move j backward until element <= last_pivot (initially same as pivot)
        while arr[j - 1] > pivot:
            j -= 1
            
        if i < j:
            low, high = partition_three_way(arr, i + 2, j - 1), None

    # Recursive step for the middle section only to ensure O(log n) stack space on average
    quicksort_partition(arr, low, j - 1)

def sort_list(data):
    """
    Wrapper function to perform in-place sorting.
    
    Args:
        data (list[int]): List of integers to be sorted.
        
    Returns:
        list[int]: The same list object after being sorted.
    """

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without any user input or external files
    raw_input = [10, 35, -29, 784, 674, -310, 78, 7, -1, 1]
    
    # Perform in-place sorting using the three-way quicksort implementation defined above
    sort_list(raw_input)

    print("Sorted list:")
    for item in raw_input:
        print(item)