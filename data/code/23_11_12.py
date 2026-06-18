def compare_and_report(list1: list[int], list2: list[int]) -> tuple[list[int], int, str]:
    """
    Compares two lists of integers by their sum.
    
    Args:
        list1 (list[int]): First list of integers.
        list2 (list[int]): Second list of integers.
        
    Returns:
        tuple[(list[int], int), int, str]: A tuple containing:
            - The first input list and its calculated sum as a tuple [list1, sum_list1].
            - An integer representing the difference between list2's sum and list1's sum (sum_list2 - sum_list1).
              If positive, it means list2 is larger; if negative or zero, list1 is greater or equal.
            - A string indicating which list has the larger sum ('list1' or 'list2').

    Time Complexity: O(n + m) where n and m are the lengths of list1 and list2 respectively.
    Space Complexity: O(1).
    """
    # Calculate sums directly without intermediate variables to minimize memory overhead, though in Python 
    # this is negligible compared to object creation costs. Using sum() is efficient due to C implementation.
    
    sum_list1 = 0
    
    for num in list1:
        sum_list1 += num
        
    sum_list2 = 0
    
    for num in list2:
        sum_list2 += num
        
    # Determine the winner based on sums
    if sum_list1 > sum_list2:
        return (list1, sum_list1), sum_list2 - sum_list1, 'list1'
    else:
        return (list2, sum_list2), sum_list1 - sum_list2, 'list2'

if __name__ == '__main__':
    # Hard-coded sample values ensuring no external input or files are needed.
    list_a = [3, 5, 7]
    list_b = [4, 6, 8, 10]

    result_data, diff_value, winner_name = compare_and_report(list_a, list_b)
    
    print(f"Comparison Results:")
    print(f"{result_data[0]} has a sum of {result_data[1]}.")
    if isinstance(result_data, tuple):
        # The function returns (list_with_sum, diff, winner). 
        # We unpack the first element which is itself a list and its sum.
        winning_list = result_data[0]
        winning_sum = result_data[1]
        
        print(f"The other list ({winning_list}) has a sum of {diff_value}.")
    else:
        print("Unexpected return format.")

    if winner_name == 'list2':
        print(f"List B wins with the larger total value, exceeding A by {abs(diff_value)} units.")
    elif diff_value <= 0:
        # This case handles equality or list1 winning (though logic above ensures correct assignment)
        pass 
    else:
        print(f"List A ({winning_list}) has a sum of {result_data[1]}, exceeding B by {abs(diff_value)} units.")