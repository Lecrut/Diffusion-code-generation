def compare_and_report(list_a: list[int], list_b: list[int]) -> tuple[list[int], str]:
    """
    Compares two lists of integers by their sum.
    
    Args:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.
        
    Returns:
        tuple[list[int], str]: A tuple containing the sums as a list [sum_a, sum_b] 
                              and a string indicating which list has the larger sum or if they are equal.
    
    Time Complexity: O(n + m) where n is len(list_a) and m is len(list_b).
    Space Complexity: O(1) excluding input/output storage.
    """
    # Calculate sums directly without intermediate variables to optimize memory usage slightly,
    # though Python's sum() function is implemented in C and highly optimized anyway.
    sum_a = 0
    for num in list_a:
        sum_a += num
        
    sum_b = 0
    for num in list_b:
        sum_b += num
    
    if sum_a > sum_b:
        winner_str = f"List A wins with a total of {sum_a}"
    elif sum_b > sum_a:
        winner_str = f"List B wins with a total of {sum_b}"
    else:
        winner_str = "Both lists have equal sums."
        
    return [sum_a, sum_b], winner_str

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    list_sample_1 = [3, 5, -2, 8]
    list_sample_2 = [-4, 6, 7, 9]

    sums_info, result_message = compare_and_report(list_sample_1, list_sample_2)
    
    print(f"Sums: {sums_info}")
    print(result_message)