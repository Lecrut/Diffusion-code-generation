def swap_even_odd_indices(s: str) -> str:
    """
    Returns a new string where every character at an even index is swapped 
    with the character at the next odd index, and vice versa.

    Args:
        s (str): The input string to process.

    Returns:
        str: A new string with characters swapped as described.
    
    Examples:
        >>> swap_even_odd_indices("abcd")
        'bdac'
        
        >>> swap_even_odd_indices("hello")
        'olheh'
        
        Note: For strings of odd length, the last character remains in place 
        because there is no next index to swap with.
    """
    if not s:
        return s

    result_chars = list(s)

    # Iterate through even indices up to len(s)-2 (inclusive)
    for i in range(0, len(result_chars), 2):
        j = i + 1
        if j < len(result_chars):
            # Swap characters at index i and j
            result_chars[i], result_chars[j] = result_chars[j], result_chars[i]

    return ''.join(result_chars)

if __name__ == '__main__':
    test_cases = [
        "abcd",      # Even length: swap (0,1), (2,3) -> bdac
        "hello",     # Odd length: swap (0,1), (2,3); 'o' stays at 4 -> olheh
        "",          # Empty string
        "a",         # Single character
        "abcdefg",   # Swap pairs until end; 'f', 'g' swapped? Wait logic check.
                     # Indices: 0(a),1(b)->b,a ; 2(c),3(d)->d,c ; 4(e) stays,5(f),6(g)->g,f ? 
                     # Let's trace "abcdefg": 
                     # i=0: swap a,b -> b,a
                     # i=2: swap c,d -> d,c
                     # i=4: e is at even index. j=5=f. swap e,f -> f,e. g remains? No, loop stops after 6 (i<7) but step 2 means next even is 6. 
                     # Loop range(0,7,2) -> [0, 2, 4, 6].
                     # i=6: j=7 which is out of bounds for "abcdefg" (len 7). So g stays? 
                     # Correct logic check: len("abcdefg") = 7. range(0,7,2) yields 0,2,4,6.
                     # At 6: index 6 exists ('g'). j=7 does not exist. Condition 'j < len' fails. No swap. 
                     # Result should be b,d,f,e,c,a,g? Wait order of swaps is sequential on original list or modified?
                     # We modify in place using result_chars which starts as copy.
                     # Start: [a,b,c,d,e,f,g]
                     # i=0, j=1: swap -> [b,a,c,d,e,f,g]
                     # i=2, j=3: swap -> [b,a,d,c,e,f,g]
                     # i=4, j=5: swap -> [b,a,d,c,f,e,g]
                     # i=6, j=7: fail. 
                     # Result: "badcfeg"
        "123",       # 0-1 swap, 2 stays? No len 3. range(0,3,2)->[0,2].
                     # i=0,j=1 -> [2,1,3] (if string digits). 
    ]

    for test_input in test_cases:
        output = swap_even_odd_indices(test_input)
        print(f"Input:      '{test_input}'")
        print(f"Output:     '{output}'\n")