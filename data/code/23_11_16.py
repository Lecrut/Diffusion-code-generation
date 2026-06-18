def compare_and_report(list_a: list[int], list_b: list[int]) -> tuple[list[int], str]:
    """
    Compares two lists of integers by their sums.
    
    Returns a tuple containing (sum_list_a, result_string), 
    where the result string indicates which sum is larger or if they are equal.
    
    Args:
        list_a: First list of integers.
        list_b: Second list of integers.
        
    Returns:
        Tuple of (int_sum_of_list_a, "string describing outcome").
    """
    # Calculate sums using a simple loop which is efficient for large lists
    sum_a = 0
    sum_b = 0
    
    for num in list_a:
        sum_a += num
        
    for num in list_b:
        sum_b += num
        
    if sum_a > sum_b:
        return [sum_a], f"List A wins with a larger sum ({sum_a} vs {sum_b})"
    elif sum_b > sum_a:
        return [sum_b], f"List B wins with a larger sum ({sum_b} vs {sum_a})"
    else:
        return [sum_a, sum_b], "Both lists have equal sums."

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    list_sample_1 = [3, 5, -2, 8, 1]
    list_sample_2 = [-4, 6, 9, -10, 7]

    result_sums_a, report_text = compare_and_report(list_sample_1, list_sample_2)
    
    print(f"Sum of List A: {result_sums_a}")
    print(report_text)