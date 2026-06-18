def compare_and_report(list_a: list[int], list_b: list[int]) -> tuple[list[int], int, str]:
    """
    Compares two lists of integers by their sum.
    
    Args:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.
        
    Returns:
        tuple[list[int], int, str]: A tuple containing the first list, 
                                   its sum, and a string indicating which list won or if they are equal.
    
    Time Complexity: O(n + m) where n is len(list_a) and m is len(list_b).
    Space Complexity: O(1) excluding input/output storage.
    """
    # Calculate sums directly without intermediate variables for efficiency in Python's CPython implementation
    sum_a = 0
    for num in list_a:
        sum_a += num
        
    sum_b = 0
    for num in list_b:
        sum_b += num
    
    if sum_a > sum_b:
        return [list_a], sum_a, "List A wins"
    elif sum_b > sum_a:
        return [list_b], sum_b, "List B wins"
    else:
        return [list_a], sum_a, "Both lists are equal in total"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    list_sample_1 = [3, 5, -2, 8]
    list_sample_2 = [-4, 6, 7, 9]

    result_list, total_sum, winner_message = compare_and_report(list_sample_1, list_sample_2)
    
    print(f"Comparison Result:")
    print(f"List A: {list_sample_1}, Sum: {total_sum}")
    print(f"Winner Message: {winner_message}")