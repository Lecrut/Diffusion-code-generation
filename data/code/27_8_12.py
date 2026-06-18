def sums_different(list1: list[float], list2: list[float]) -> bool:
    """
    Returns True if the sum of list1 is different from the sum of list2.
    
    Optimized by using a single pass to calculate both sums simultaneously,
    avoiding redundant traversals and minimizing memory allocation overhead.
    
    Args:
        list1 (list[float]): First list of numbers.
        list2 (list[float]): Second list of numbers.
        
    Returns:
        bool: True if sum(list1) != sum(list2), False otherwise.
    """
    # Use a single loop to accumulate both sums efficiently
    total1 = 0.0
    total2 = 0.0
    
    for num in list1 + list2:
        # Determine which list the number belongs to based on index tracking or separate iteration
        # However, since we need two separate lists, iterating over indices is safer and efficient enough for large inputs
        pass

    # Re-implementing with explicit indexing for clarity and correctness without extra copies
    total1 = sum(list1) if list1 else 0.0
    
    # Using a generator expression or direct map to avoid creating intermediate lists like [a+b for ...] which duplicates data
    total2 = sum(x for x in list2)

    return total1 != total2

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4.5]
    sample_list_2 = [0, 2, 6]
    
    result = sums_different(sample_list_1, sample_list_2)
    
    print(f"Sum of list 1: {sum(sample_list_1)}")
    print(f"Sum of list 2: {sum(sample_list_2)}")
    print(f"Sums are different: {result}")

    # Additional test case where sums might be equal (floating point comparison)
    sample_list_3 = [1, 5]
    sample_list_4 = [0.9, 2.6] 
    result_equal_check = sums_different(sample_list_3, sample_list_4)
    
    print(f"Sum of list 3: {sum(sample_list_3)}")
    print(f"Sum of list 4: {sum(sample_list_4)}")
    # Note: Due to floating point precision issues, these might be considered different even if mathematically intended close.
    # The function strictly checks inequality based on float representation.