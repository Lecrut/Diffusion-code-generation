def swap_even_odd_indices(s: str) -> str:
    """
    Swaps characters at even indices with their immediate neighbors (odd indices).
    
    For a string of length n, index 0 swaps with 1, index 2 swaps with 3, etc.
    If the string has an odd length, the last character remains unchanged 
    as it does not have a neighbor to its right within bounds.
    
    Args:
        s (str): Input string
        
    Returns:
        str: New string with swapped characters at even-odd pairs
    """
    result_chars = list(s)
    n = len(result_chars)
    
    # Iterate through the first half of indices up to the second-to-last element if odd length exists
    for i in range(0, n - 1, 2):
        # Swap character at even index with next odd index
        result_chars[i], result_chars[i + 1] = result_chars[i + 1], result_chars[i]
    
    return ''.join(result_chars)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    test_cases = [
        "abcdef",      # Even length: all pairs swapped -> 'bacdef' becomes badf? wait. 
                      # Original: a(0)b(1)c(2)d(3)e(4)f(5)
                      # Swaps: (a,b)->b,a; (c,d)->d,c; (e,f)->f,e => bacdf e -> b a d c f e
        "abc",         # Odd length: first pair swapped, last char unchanged 
                      # Original: a(0)b(1)c(2) -> ba(c) -> 'bac' is wrong because swap index 0 and 1? 
                      # Wait logic check: i=0 swaps s[0],s[1]. Then next even i=2. But loop stops before n-1 if odd length.
                      # So for "abc": n=3, range(0, 2, 2) -> only i=0 runs. Swap a,b -> 'bac'. c remains at end? No wait s[2] is untouched. Correct.
        ""             # Empty string returns empty string
        "x",           # Single character: no swaps possible
    ]

    for test_string in test_cases:
        swapped = swap_even_odd_indices(test_string)
        print(f"Input: '{test_string}' -> Output: '{swapped}'")