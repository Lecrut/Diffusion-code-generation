def swap_even_odd_indices(s: str) -> str:
    """
    Swaps characters at even indices with their neighbors (odd indices).
    For a string of length n, this swaps s[0] <-> s[1], s[2] <-> s[3], etc.
    
    If the string has odd length, the last character remains in place 
    since it cannot be paired with an index beyond the string bounds.

    Args:
        s (str): Input string to process.

    Returns:
        str: String with even and odd indexed characters swapped.
    """
    result = list(s)
    
    # Iterate through indices in steps of 2 up to len(result)-1 if length is odd
    for i in range(0, len(result), 2):
        j = i + 1
        if j < len(result):
            # Swap even index character with next (odd) index character
            result[i], result[j] = result[j], result[i]

    return ''.join(result)

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required
    
    test_cases = [
        "abcdef",      # Even length: swaps a-b, c-d, e-f -> bacdfE (wait: b-a, d-c, f-e) -> ba dc fe -> badcfe? Let's trace carefully. 
                      # Original: 0:a,1:b,2:c,3:d,4:e,5:f
                      # Swap pairs: (a,b)->(b,a), (c,d)->(d,c), (e,f)->(f,e)
                      # Result: b a d c f e -> "badcf" wait no. 
                      # Input: abcd ef? No input is "abcdef". 
                      # 0:a,1:b => swap => ba; 2:c,3:d => dc; 4:e,5:f => fe
                      # Result string: badcfe
    
        "abcde",       # Odd length: a-b swapped, c-d swapped, e stays. -> bacdE? No: b-a d-c e -> "badce"
    
        "",             # Empty string
        "a",            # Single character, no change possible
        "ab",           # Two characters swap
    
    ]

    for test_input in test_cases:
        output = swap_even_odd_indices(test_input)
        print(f"Input: '{test_input}' -> Output: '{output}'")