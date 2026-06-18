def check_sum_difference(list1: list[float], list2: list[int]) -> bool:
    """
    Returns True if the sum of elements in list1 is different from the sum 
    of elements in list2. Designed with efficiency in mind for large inputs by using direct summation without intermediate data structures where possible.

    Parameters:
        list1 (list[float]): First list of numbers, which can contain floating-point values.
        list2 (list[int]): Second list of integers.

    Returns:
        bool: True if sum(list1) != sum(list2), False otherwise.
    """
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    # Sample values - no user input, network access, or file dependencies required
    list_a = [30, 40, 50]          # Sum: 120
    list_b = [10, 20, 60]         # Sum: 90
    
    result = check_sum_difference(list_a, list_b)
    
    print(f"List A sum: {sum(list_a)}")
    print(f"List B sum: {sum(list_b)}")
    print(f"Differing sums? {result}")