def sums_are_different(list_a: list[float], list_b: list[int]) -> bool:
    """
    Returns True if the sum of numbers in list_a is different from 
    the sum of numbers in list_b. Optimized using built-in sum() for efficiency.
    
    Args:
        list_a (list): List of numeric values.
        list_b (list): List of integer or numeric values.
        
    Returns:
        bool: True if sums differ, False otherwise.
    """
    return sum(list_a) != sum(list_b)

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = [5, 6, 7]

    result = sums_are_different(sample_list_1, sample_list_2)
    
    if result:
        print("The sums are different.")
    else:
        print("The sums are the same.")