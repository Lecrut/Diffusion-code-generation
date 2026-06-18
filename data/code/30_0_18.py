def swap_characters(s: str) -> str:
    """
    Swaps every adjacent pair of characters in a string in place (conceptually, 
    as strings are immutable, returns the new string with swaps applied).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string where every two adjacent characters have been swapped.
             Note: While the docstring says "in place", Python strings are immutable.
             This function returns the modified sequence of characters as a new string,
             which is the standard efficient approach in Python for this operation.
    """
    # Convert to list for mutability during processing if needed, 
    # but since we need to return and swap pairs efficiently:
    chars = list(s)
    
    n = len(chars)
    i = 0
    
    while i < n - 1:
        # Swap adjacent pair at index i and i+1
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
        i += 2
        
    return ''.join(chars)

if __name__ == '__main__':
    test_cases = [
        "abcdef",      # Expected: bacdef -> b a c d e f (swapped pairs: ab->ba, cd->dc, ef->fe? No. Pairs are indices 0-1, 2-3, etc.)
                      # Input: a,b,c,d,e,f 
                      # Pair 1: a,b -> b,a
                      # Pair 2: c,d -> d,c
                      # Result: badc fe (badcef) - Wait, let's trace carefully.
                      # indices: 0:a, 1:b, 2:c, 3:d, 4:e, 5:f
                      # swap(0,1): b,a; swap(2,3): d,c; swap(4,5): f,e -> badcef? 
                      # Actually: a,b becomes b,a. c,d becomes d,c. e,f becomes f,e. Result: badcfe.
        "hello",       # h,l -> l,h ; e,o (no pair) -> heo ? No. 
                      # 0:h,1:l -> l,h; 2:e,3:o-> o,e; 4:l remains. Result: lhoe l? -> lhoel?
                      # Let's re-verify logic manually for "hello":
                      # i=0: swap h,l -> l,h. List: [l, h, e, o, l] (Wait index 2 is 'e', 3 is 'o')
                      # Correct trace: 
                      # s = "hello"
                      # chars = ['h','e','l','l','o'] -- Wait spelling error in thought. hello -> h,e,l,l,o
                      # i=0: swap e,h? No, index 1 is 'e'. Pair (0,1) is ('h','e') -> ('e','h'). List: ['e', 'h', ...]
                      # Next pair indices (2,3): ('l','l') -> ('l','l'). 
                      # Last char at 4 remains. Result: ehll o? -> ehllo.
        "a"             # Single character, no pairs possible. Returns same string.
    ]

    for test_input in test_cases:
        result = swap_characters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result}'\n")