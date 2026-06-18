def sums_are_different(list1: list[int], list2: list[float]) -> bool:
    """
    Returns True if the sum of elements in list1 is different from 
    the sum of elements in list2, otherwise returns False.
    
    Optimized for large inputs by using a single pass to calculate sums.
    Handles both integer and float inputs (integers are converted internally).

    Args:
        list1 (list[int]): First list containing integers or floats.
        list2 (list[float]): Second list containing floats or ints.

    Returns:
        bool: True if sum(list1) != sum(list2), False otherwise.
    """
    # Using built-in sum is implemented in C and highly optimized for large lists,
    # which makes it faster than a manual loop in Python interpretation overhead.
    return sum(map(float, list1)) != sum(list2)

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = [5, 45]

    result = sums_are_different(sample_list_1, sample_list_2)
    
    # Output the boolean result to verify correctness without external input
    print(result)