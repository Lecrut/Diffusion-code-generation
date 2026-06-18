def compare_and_report(list_a: list[int], list_b: list[int]) -> dict[str, int]:
    """
    Determines which of two lists has a larger sum.
    
    Args:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.
        
    Returns:
        dict with keys 'sum_a', 'sum_b', and 'winner'. 
        If sums are equal, the winner is None.
    
    Time Complexity: O(n + m) where n and m are lengths of list_a and list_b respectively.
    Space Complexity: O(1).
    """
    sum_a = 0
    for value in list_a:
        sum_a += value
        
    sum_b = 0
    for value in list_b:
        sum_b += value
    
    if sum_a > sum_b:
        winner_name = "List A"
    elif sum_b > sum_a:
        winner_name = "List B"
    else:
        winner_name = None
        
    return {
        'sum_a': sum_a,
        'sum_b': sum_b,
        'winner': winner_name
    }

if __name__ == '__main__':
    sample_list_1 = [3, -2, 5, 0]
    sample_list_2 = [-7, 8, 4, -9]
    
    result = compare_and_report(sample_list_1, sample_list_2)
    
    print(f"Sum of List A: {result['sum_a']}")
    print(f"Sum of List B: {result['sum_b']}")
    
    if result['winner'] == "List A":
        print("Winner is List A")
    elif result['winner'] == "List B":
        print("Winner is List B")
    else:
        print("Both lists have equal sums.")