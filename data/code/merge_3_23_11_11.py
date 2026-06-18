def compare_and_report(list_a: list[int], list_b: list[int]) -> tuple[list[int], int, str]:
    """
    Compares two lists of integers by their sum.
    
    Args:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.
        
    Returns:
        tuple[list[int], int, str]: A tuple containing the first list, 
                                   its sum, and a message indicating which list is larger or if they are equal.
    
    Time Complexity: O(n + m) where n and m are the lengths of list_a and list_b respectively.
    Space Complexity: O(1) as no additional data structures proportional to input size are used beyond simple accumulators.
    """
    sum_a = 0
    for num in list_a:
        sum_a += num
        
    sum_b = 0
    for num in list_b:
        sum_b += num
    
    if sum_a > sum_b:
        message = f"{list_a} wins with a larger sum of {sum_a}"
    elif sum_b > sum_a:
        message = f"{list_b} wins with a larger sum of {sum_b}"
    else:
        message = "Both lists have equal sums"
        
    return list_a, sum_a, message

if __name__ == '__main__':
    sample_list_1 = [3, 5, -2, 7]
    sample_list_2 = [-4, 8, 6, 9]
    
    winner_list, total_sum_winner, report_message = compare_and_report(sample_list_1, sample_list_2)
    
    print(f"Report: {report_message}")