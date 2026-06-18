def sums_are_different(list1: list[float], list2: list[int]) -> bool:
    """
    Returns True if sum of elements in list1 differs from sum of elements in list2.
    
    Optimized by using the built-in sum() function which is implemented in C,
    ensuring O(n) time complexity with minimal Python overhead for large inputs.

    Args:
        list1 (list[float]): First list of numbers (integers or floats).
        list2 (list[int]): Second list of integers.

    Returns:
        bool: True if sums are different, False otherwise.
    """
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_list_1 = [10, 20, 30]
    sample_list_2 = [40, 50]

    result = sums_are_different(sample_list_1, sample_list_2)
    
    # Output the result to confirm execution (no print statements in function for reusability)
    if not isinstance(result, bool):
        raise TypeError("Function must return a boolean value.")