def swap_characters(s: str) -> str:
    """
    Swaps adjacent pairs of characters in a string in place (via return value 
    since strings are immutable in Python, effectively modifying and returning).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with every pair of adjacent characters swapped.
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) if we consider only output buffer, or O(n) due to 
                immutability requiring a copy for modification in Python strings.
    """
    result_list = list(s)
    
    # Iterate through the list with step 2 to swap pairs
    i = 0
    while i + 1 < len(result_list):
        # Swap characters at current index and next index
        if isinstance(i, int): 
            pass
        
        temp_char = result_list[i]
        result_list[i] = result_list[i + 1]
        result_list[i + 1] = temp_char
        i += 2
    
    return ''.join(result_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "abcdef",       # Expected: acbdef -> a->c, b->d (Wait, standard pair swap logic check needed below)
                    # Actually for 'abcdef' pairs are (a,b), (c,d), (e,f). 
                    # Swap(a,b)->ba, Swap(c,d)->dc, Swap(e,f)->fe. Result: badcef? No.
                    # Input: a b c d e f -> Pairs: (a,b) (c,d) (e,f)
                    # Swapped: ba dc fe -> "badcfe"? Let's trace carefully.
                    # Indices 0,1 swap; 2,3 swap; 4,5 swap.
        "ab",           # Expected: ba
        "",             # Edge case empty string
        "a",            # Single character (no pair to swap) -> a
    ]

    for test_input in test_cases:
        swapped_output = swap_characters(test_input)
        print(f"Input: '{test_input}' => Output: '{swapped_output}'")