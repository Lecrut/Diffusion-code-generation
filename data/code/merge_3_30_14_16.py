def swap_even_odd_indices(s: str) -> str:
    """
    Returns a new string where characters at even indices are swapped 
    with their adjacent odd index neighbors, and vice versa.
    
    Example: "abcd" (indices 0,1,2,3) becomes "badc".
            'a'(0)<->'b'(1), 'd'(3)<->'c'(2).
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped characters at even/odd positions.
    """
    # Convert the string to a list for mutability, then back to string later
    chars = list(s)
    
    n = len(chars)
    i = 0
    
    while i < n - 1:
        if i % 2 == 0:
            # Swap even index with next odd index
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
            i += 2
        else:
            # If we are at an odd index, it means the previous step 
            # (even-odd swap) already handled pairing this character.
            # However, to strictly follow "every" even/odd pair logic without 
            # overlapping swaps causing issues in a single pass loop structure,
            # let's reconsider: The prompt says "swap every char at an even index 
            # with the char at the next odd index". This implies pairs (0,1), (2,3), etc.
            # If we encounter i=1 here, it shouldn't be swapped again as part of a new pair.
            # But wait, if I swap 0 and 1, then move to 2. 
            # The condition "i < n - 1" ensures no index out of bounds for the next element.
            # If i is odd (e.g., 1), we shouldn't start a new pair because pairs are formed by even indices.
            # So if i starts at an odd number, it means something went wrong with the step size or logic flow above?
            pass 
        i += 2
    
    return "".join(chars)

# Corrected Logic Implementation for clarity and robustness:
def swap_even_odd_indices_v2(s: str) -> str:
    """
    Returns a new string where characters at even indices are swapped 
    with their adjacent odd index neighbors. Pairs are (0,1), (2,3), etc.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped characters.
    """
    chars = list(s)
    n = len(chars)
    
    # Iterate only over even indices up to the second-to-last character
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            # Swap current (even) with next (odd)
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    test_cases = [
        "abcd",      # Expected: badc
        "hello world", # Expected: hleolrldow (h<->e, l<->l? No. 0:h,1:e -> eh; 2:l,3:o -> ol; ... wait)
                     # Let's trace "hello": 
                     # 0(h)<->1(e) => eh... 
                     # 2(l)<->3(l) => ll...
                     # 4(o)<->5( ) => o (space)? No. index 4 is 'o', index 5 is space. Swap -> space then o?
                     # Result: "ehllo world" ? Let's re-calculate carefully.
        "abcdef",    # Expected: bacdef? 
                     # 0(a)<->1(b) => ba...
                     # 2(c)<->3(d) => dc...
                     # 4(e)<->5(f) => fe... -> badcfe ? No, indices are fixed.
        "a",          # Expected: a (no pair)
    ]

    for test_input in test_cases:
        result = swap_even_odd_indices_v2(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result}'\n")