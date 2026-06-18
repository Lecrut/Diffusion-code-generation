def compare_and_report(list_a: list[int], list_b: list[int]) -> tuple[list[int] | None, int, str]:
    """
    Compares two lists of integers based on their sums and reports the result.
    
    Parameters:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.
        
    Returns:
        tuple[list[int] | None, int, str]: A tuple containing:
            - The sum of the winning list or None if sums are equal.
            - The difference between the larger and smaller sum (positive for winner).
            - A descriptive string stating which list won and by how much.
    """
    total_a = sum(list_a)
    total_b = sum(list_b)

    # Determine which is greater, handling potential overflow not expected in standard Python ints but logically sound regardless of size
    if total_a > total_b:
        return None, total_a - total_b, f"List A wins with a difference of {total_a - total_b}."
    elif total_b > total_a:
        return list_b, total_b - total_a, f"List B wins by a margin of {total_b - total_a}."
    else:
        return None, 0, "Both lists have equal sums; no winner."

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes. No user input required.
    list_one = [10, 25, -5, 3]
    list_two = [7, 8, 9, 4, 6]

    winning_list_result, diff_strictness, message_reported = compare_and_report(list_one, list_two)

    print(f"Comparison Report:")
    print(f"Difference magnitude: {diff_strictness}")
    
    if winning_list_result is not None:
        # If one wins, we should return it as the third item in tuple but actually we are returning three things from function call above? 
        # Actually looking back at signature and logic: returns (None/WinningList, DiffStricctness, Message)
        print(f"Winner List Content: {winning_list_result}")
    else:
        print("Result:")
    
    print(message_reported)

# The above structure ensures compliance with the return tuple format expected by caller logic. 
# However, re-reading task requirement "returning the sums and the winning list".
# My current implementation returns (winning_list_or_none, difference, message).
# Let's refine slightly to strictly match 'sums' and 'winning list' in a cleaner tuple if needed?
# The prompt says: returning the sums AND the winning list. 
# It does not explicitly forbid additional return values like diff or message but implies those are core outputs.
# Given "returning the sums and the winning list", I will adjust slightly to be more direct about what is requested while keeping efficiency, maybe adding a descriptive object?
# No simpler approach: Let's ensure we definitely provide sums and winner clearly.

    # Re-evaluating return value for clarity based on prompt: 
    # "returning the sums and the winning list" -> Could interpret as returning (sum_a, sum_b, winner_list) or similar.
    # But also needs to determine WHICH is larger. So maybe tuple of (sums_tuple, winning_list).
    
    # Let's stick to a clean output that satisfies "returning sums AND winning list". 
    # If no clear winner, return None for the third element? Or just sum_a and sum_b if equal?
    
    # Revised plan: Return a tuple of (sums_dict_or_tuple, winning_list).
    # But earlier code was fine. Let's ensure we output sums explicitly somewhere too or in logic flow.
    # Actually, let's make the return signature very explicit to avoid ambiguity. 
    # Return type hint should reflect "sums" and "winning list". 
    
    # New approach for main block:
    
    result_data = compare_and_report(list_one, list_two)