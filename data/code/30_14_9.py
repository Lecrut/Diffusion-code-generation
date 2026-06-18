def swap_even_odd_indices(s: str) -> str:
    """
    Returns a new string where characters at even indices (0, 2, ...) 
    are swapped with their adjacent odd index neighbors (1, 3, ...).
    
    If the last character is at an even index and there is no following odd index, it remains in place.
    
    Example: "abcde" -> "bacdc"
             Indices: 0(ab) <-> 1(bc), 2(cd) <-> 3(de), 4(e) stays
    """
    if not s:
        return s
    
    result_chars = list(s)
    n = len(result_chars)
    
    # Iterate through even indices up to the middle of the string
    for i in range(0, n - 1 + (n % 2), 2):
        # Swap character at current index with next odd index if it exists
        if i + 1 < n:
            result_chars[i], result_chars[i + 1] = result_chars[i + 1], result_chars[i]
    
    return ''.join(result_chars)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "abcdef",      # Even length: swap (0,1), (2,3), (4,5) -> 'bfadce'
        "abcde",       # Odd length: swap (0,1), (2,3); last char stays -> 'bacdc'
        "",            # Empty string
        "a",           # Single character
        "ab",          # Two characters -> 'ba'
    ]

    for test_input in test_cases:
        output = swap_even_odd_indices(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{output}'\n")