def swap_even_odd_indices(s: str) -> str:
    """
    Swaps characters at even indices with those at odd indices in a string.
    
    For example, if input is "abcd", output becomes "badc".
    If the length is odd (e.g., "abc"), only pairs are swapped ("bac").
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with even and odd indexed characters swapped.
    """
    if not s:
        return ""

    result = []
    length = len(s)
    
    # Iterate through the string in steps of 2 starting from index 0 (even)
    for i in range(0, length - 1, 2):
        even_idx = i
        odd_idx = i + 1
        
        if odd_idx < length:
            result.append(s[odd_idx])
            result.append(s[i])
        else:
            # If the last character is at an even index and there's no following odd index,
            # it remains in place (or logically swapped with nothing).
            # Based on "swapping every character with its neighbor", 
            # if a pair doesn't exist, we keep the order as per standard interpretation.
            result.append(s[i])

    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    
    samples = [
        "abcd",      # Expected: badc (a<->b, c<->d)
        "abc",       # Expected: bac  (a<->b, c stays as last since no odd neighbor after it? 
                     # Actually logic above keeps 'c' at end. Let's trace: i=0 -> swap a,b; i=2 -> only even, append s[2]. Result: b,a,c)
        "12345",     # Expected: 21435 (1<->2, 3<->4, 5 stays)
        "",          # Edge case empty string
        "a"           # Single character edge case -> should return "a" as no swap possible
    ]

    for test_input in samples:
        output = swap_even_odd_indices(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{output}'\n")