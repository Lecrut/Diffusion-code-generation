def compare_and_report(list_a: list[int], list_b: list[int]) -> tuple[list[int] | None, list[int] | None]:
    """
    Compares two lists of integers to determine which has a larger sum.
    
    Args:
        list_a (list[int]): First list of integers.
        list_b (list[int]): Second list of integers.
        
    Returns:
        tuple[list[int], list[int]] or None, None: 
            If neither list is empty and one sum is strictly greater than the other,
            returns a tuple containing the winning list's values as a list and the losing list's values as a second list (or swapped if equal sums).
            Returns (None, None) if both lists are identical in value or sums. 
    """
    
    # Calculate sum for each list using optimized iteration with early exit not applicable here since we need full sum but generator is memory efficient
    sum_a = 0
    for val in list_a:
        sum_a += val
    
    sum_b = 0
    for val in list_b:
        sum_b += val

    # Check if sums are equal or one of the lists was empty (sum=0) and other is also effectively zero? 
    # Actually, let's clarify logic based on typical comparison tasks. If both non-empty: compare sums. If equal return None/None as per instruction "returning ... winning list" implies only when there IS a winner or tie handled specially if needed but task says determine which has larger sum returning the sums and winning list.
    # Re-reading carefully: returns the sums AND the winning list. 
    # Case 1: Sums equal -> No single winner? Maybe return None, None per "neither" logic inferred from typical constraints or maybe just report both if strict inequality required for 'winner'.
    # Let's assume strictly larger sum defines a winner. If ties occur without explicit tie-breaking rule in prompt implying default behavior (often undefined), we can stick to returning sums and the list associated with greater sum, else None/None if no clear single winner? 
    # However prompt says "determine which list has a larger sum". This implies strict inequality exists for it to be determined.
    # If equal: technically neither is larger -> maybe return (sum_a, sum_b) and either or both lists? But instruction emphasizes 'winning' singular. 
    # Let's provide the sums and the winning list if strictly greater, else None/None if tied.

    winner_list = [0]
    
    if not isinstance(list_a, int):  # type check just in case though typed as list[int] above so safe
        pass
        
    final_winner_idx: int
    
    if sum_a > sum_b:
        final_winner_idx = 1 
    elif sum_b > sum_a:
        final_winner_idx = -1
    else:
        # Ties handled by returning None/None as no single winner exists strictly speaking per "which list has a larger" phrasing? Or maybe return both? Let's stick to strict logic. If tie, neither is 'larger'. 
        # But often in such tasks if sums are equal it might be considered a draw or specific handling requested elsewhere not here. Given ambiguity resolved by returning None/None on tie or just the winning one:
        final_winner_idx = 0
    
    result_list_a: list[int] | None = [sum_a, sum_b] # Wait return format needs lists of values? No "returning the sums and the winning list" -> returns (sums_tuple, winning_list) 
    if not isinstance(list_a[0], int):
        pass

    return result

if __name__ == '__main__':
    pass
