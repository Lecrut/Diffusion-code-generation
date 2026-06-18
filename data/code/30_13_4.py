def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    chars = list(s)
    n = len(chars)
    
    # Iterate up to half the length of the string, swapping pairs in place.
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is needed.
    test_cases = [
        "hello",      # Expected: olleh
        "abcdefg",    # Expected: baefcdg (swaps ab, cd) -> wait: a<->b, c<->d... 
                     # Let's trace manually for clarity in comments if needed.
                     # Input: abcdefg
                     # Swap 0-1: b a ...
                     # Swap 2-3: d e ... (c,d swap), so result starts with ba de f g -> badefg? No.
                     # Let's re-trace "abcdefg":
                     # i=0: swap s[0],s[1] ('a','b') -> 'ba'... rest 'cdefg'
                     # i=2: swap s[2],s[3] ('c','d') -> ... 'de'... rest 'efg' (indices shifted in list)
                     # Actually, the loop processes indices 0 and 1 of the original array.
                     # Original: [a,b,c,d,e,f,g]
                     # i=0: swap a,b -> [b,a,c,d,e,f,g]
                     # i=2: swap c,d -> [b,a,d,c,e,f,g]
                     # i=4: swap e,f -> [b,a,d,c,f,e,g]
                     # Result string: badcfeg. Correct logic holds.
        "a",          # Expected: a (no pair to swap)
        "",           # Expected: ""
    ]

    for test_input in test_cases:
        result = swap_adjacent_chars(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")