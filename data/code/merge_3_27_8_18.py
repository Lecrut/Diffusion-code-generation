def sums_differ(list1: list[int], list2: list[int]) -> bool:
    """
    Returns True if sum of list1 is different from sum of list2, False otherwise.
    Optimized using built-in sum() for C-level iteration efficiency on large inputs.
    
    Args:
        list1 (list[int]): First list of numbers.
        list2 (list[int]): Second list of numbers.
        
    Returns:
        bool: True if sums are different, False otherwise.
    """
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5, 6, 7, 8, 9]

    result = sums_differ(sample_list_1, sample_list_2)
    
    # Print the boolean result to stdout as a demonstration of functionality
    print(result)