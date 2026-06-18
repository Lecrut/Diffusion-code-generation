def swap_characters(s: str) -> str:
    """
    Swaps adjacent pairs of characters in a string in place (conceptually, 
    as strings are immutable in Python, this returns a new string with swapped chars).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string where every pair of adjacent characters has been swapped.
             If the length is odd, the last character remains unchanged.
    """
    # Convert to list for mutability simulation or direct slicing construction
    chars = list(s)
    
    # Iterate with step 2 and swap elements at index i and i+1 if they exist
    n = len(chars)
    for i in range(0, n - 1, 2):
        # Check if there is a next character to pair with
        if i + 1 < n:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, stdin, or args)
    test_cases = [
        "abcdef",   # Expected: 'bacdef' -> wait, pairs are ab->ba, cd->dc, ef->fe? 
                   # Actually standard swap adjacent means index 0<->1, 2<->3...
                   # Input: a b c d e f
                   # Swap (a,b) -> ba; (c,d) -> dc; (e,f) -> fe. Result: badcfedf? No.
                   # Let's trace carefully: 
                   # Indices: 0,1,2,3,4,5
                   # Pair at 0: swap s[0],s[1] ('a','b') -> 'ba'
                   # Pair at 2: swap s[2],s[3] ('c','d') -> 'dc'
                   # Pair at 4: swap s[4],s[5] ('e','f') -> 'fe'
                   # Result string: "badcfed"? No, concatenation is ba + dc + fe = bad c f e? 
                   # Wait, b a d c f e. String: "bacdef" -> "b", "a", "d", "c", "f", "e". Correct logic yields "ba" then "dc" then "fe".
        "hello",    # h,e,l,o (odd length) -> ehlo? No, pairs: he->eh, lo->ol. Result: eholo? 
                   # Indices 0,1 ('h','e') swap to 'eh'. Index 2,3 ('l','o') swap to 'ol'. Last char ignored or kept as is if odd loop stops before it.
                   # My logic: range(0, 4, 2) -> i=0, i=2. 
                   # i=0: swap h,e -> e,h. List: [e, h, l, o] (wait, original was h,e,l,o? No hello is h,e,l,l,o).
                   # Let's re-eval "hello": indices 0:h, 1:e, 2:l, 3:l, 4:o.
                   # i=0: swap s[0],s[1] -> e,h. List: [e, h, l, l, o].
                   # i=2: swap s[2],s[3] -> l,l (no change). 
                   # Result: "ehll". Wait, original was hello. Pairs are he and ll. Swap he->eh. Swap ll->ll. Last 'o' stays? Yes.
                   # So result should be "ehllo"? No. e h l l o -> eh + ll + o = ehllo. 
                   # My manual trace above said "eholo" which was wrong because I misread the string or indices.
        ""          # Empty string
    ]

    for test_input in test_cases:
        result = swap_characters(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")