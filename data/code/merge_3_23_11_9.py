def compare_and_report(list_a: list[int], list_b: list[int]) -> tuple[list[int], str]:
    """
    Compares two lists of integers to determine which has a larger sum.
    
    Parameters:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.
        
    Returns:
        tuple[list[int], str]: A tuple containing the sums of both lists and 
                              a string indicating which list has the larger sum.
    
    Time Complexity: O(n + m) where n is len(list_a) and m is len(list_b).
    Space Complexity: O(1) excluding input/output storage.
    """
    # Calculate sums directly while iterating to avoid intermediate large integers if possible,
    # though Python handles arbitrary precision automatically. Using sum() for clarity 
    # as it's implemented in C and highly optimized.
    
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    
    winning_list_name = "List A" if sum_a > sum_b else ("List B" if sum_b >= sum_a else "")
    
    return [sum_a, sum_b], f"{winning_list_name} wins with a total of {max(sum_a, sum_b)}."

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external dependencies used.
    list_sample_1 = [3, 5, -2, 8, 4]
    list_sample_2 = [-10, 7, 6, -3, 9, 1]

    sums_and_winner, report_message = compare_and_report(list_sample_1, list_sample_2)
    
    print("Sums:", sums_and_winner)
    print(report_message)