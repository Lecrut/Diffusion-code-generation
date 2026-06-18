def compare_and_report(list_a, list_b):
    """
    Compares two lists of integers to determine which has a larger sum.
    
    Parameters:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.
        
    Returns:
        tuple: A 4-element tuple containing:
            - sum_of_list_a (int): Sum of elements in list_a.
            - has_larger_sum_a (bool): True if list_a's sum is larger, False otherwise.
            - sum_of_list_b (int): Sum of elements in list_b.
            - name_of_winner (str): Name ('a' or 'b') of the list with the larger sum.
    """
    
    # Use built-in sum for efficiency as it is implemented in C internally
    total_a = sum(list_a)
    total_b = sum(list_b)
    
    if total_a > total_b:
        winner_name = "a"
    else:
        winner_name = "b"

if __name__ == '__main__':
    pass
