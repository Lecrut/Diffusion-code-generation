def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of characters in the string (0 with 1, 2 with 3, etc.).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: The resulting string after performing adjacent swaps.
        
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(n) for storing the result list or converted back to string.
    """
    chars = list(s)
    
    # Iterate over the string with a step of 2
    for i in range(0, len(chars), 2):
        # Check if there is a second character to swap with
        if i + 1 < len(chars):
            # Swap characters at current and next index
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",   # Expected: "bacdef" -> wait, let's trace: a<->b => ba, c<->d => cd, e<->f => ef. Result: bacdef? No. 
                   # Original indices: 0(a),1(b),2(c),3(d),4(e),5(f)
                   # Swap (0,1): b,a | (2,3): d,c | (4,5): f,e -> "badcfe"
        "abcdef",   # Let's re-verify manually: a,b,c,d,e,f. Pair 1: a,b->b,a. Pair 2: c,d->d,c. Pair 3: e,f->f,e. Result string: badcfe.
                   # Wait, the example in prompt says "e.g., swap index 0 with 1". 
                   # So for input abcdef: 
                   # i=0 (a,b) -> b,a; i=2 (c,d) -> d,c; i=4 (e,f) -> f,e.
                   # Result string is badcfe? No, wait. 
                   # String construction: chars[0] becomes 'b', chars[1] becomes 'a'. 
                   # So yes "badcfe" seems correct logic-wise but let's double check the prompt example wording again. 
                   # The prompt says e.g., swap index 0 with 1, 2 with 3...
        "abc",      # Expected: bac (swap a,b). Index 2 is last, no pair for c. Result: bca? No. i=0 swap(0,1), next i=2 stop. 
                   # So 'a','b' swapped -> 'b','a'. 'c' stays. "bac".
        "",          # Empty string returns empty.
    ]

    test_results = []
    
    for s in sample_strings:
        result = reverse_adjacent_swaps(s)
        print(f"Input: '{s}'")
        print(f"Output: '{result}'\n")
        
        expected_outputs = [
            ("abcdef", "badcfe"), 
            ("abc", "bac"),
            ("", ""),
        ]

    # Just printing results based on manual trace to satisfy 'runnable' requirement without user input logic errors.
    print("=== Sample Execution Output ===")
    
    sample1 = reverse_adjacent_swaps("abcdef")
    print(f"Input: 'abcdef', Output: '{sample1}' (Expected: badcfe)")
    
    sample2 = reverse_adjacent_swaps("abc")
    print(f"Input: 'abc', Output: '{sample2}' (Expected: bac)")
    
    sample3 = reverse_adjacent_swaps("")