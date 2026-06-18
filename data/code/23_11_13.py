def compare_and_report(list_a: list[int], list_b: list[int]) -> tuple[list[int], int, str]:
    """
    Compares two lists of integers by their sums.
    
    Returns a tuple containing:
        - The sum of the first list (int)
        - The sum of the second list (int)
        - A string indicating which list has the larger sum
    
    Time Complexity: O(n + m), where n and m are the lengths of the two lists.
    Space Complexity: O(1).
    
    Args:
        list_a: First list of integers.
        list_b: Second list of integers.
        
    Returns:
        A tuple (sum_list_a, sum_list_b, winner_description) where 
        winner_description is either "List A" or "List B". If sums are equal, it returns "Tie".
    """
    # Calculate the sum for both lists efficiently using a single pass per list.
    sum_a = 0
    for num in list_a:
        sum_a += num
        
    sum_b = 0
    for num in list_b:
        sum_b += num
    
    if sum_a > sum_b:
        winner_desc = "List A"
    elif sum_b > sum_a:
        winner_desc = "List B"
    else:
        winner_desc = "Tie"

    return (sum_a, sum_b, winner_desc)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    list_sample_1 = [3, 5, -2, 8]
    list_sample_2 = [-10, 4, 6, 7]

    sum_a, sum_b, result_message = compare_and_report(list_sample_1, list_sample_2)
    
    print(f"Sum of List A: {sum_a}")
    print(f"Sum of List B: {sum_b}")
    print(f"Winner: {result_message}")