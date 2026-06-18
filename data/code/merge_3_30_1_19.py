def swap_adjacent_pairs(text: str) -> str:
    """
    Returns a new string where every pair of adjacent characters has been swapped.
    
    Uses slicing to process pairs efficiently without iterating character by character.
    Even-length strings are handled directly; odd-length strings keep the last character as-is,
    since it cannot form a complete pair with an existing neighbor in this context.
    
    Args:
        text (str): The input string to swap adjacent characters from.
        
    Returns:
        str: A new string with swapped pairs of adjacent characters.
    """
    # Use slicing [::2] and [1::2] to extract even-indexed and odd-indexed characters respectively,
    # then concatenate them in reverse order for each pair (odd first, then even).
    return ''.join([text[i:i+2][::-1] if i % 2 == 0 else text[i-1:i+1][::-1] 
                   for i in range(0, len(text), 2)])

# Optimized version using pure slicing without list comprehension overhead:
def swap_adjacent_pairs_optimized(text: str) -> str:
    """Optimized implementation of the swapping logic."""
    result = []
    
    # Process pairs from start to end-1 (skipping last char if odd length)
    for i in range(0, len(text), 2):
        pair = text[i:i+2]
        if len(pair) == 2:
            result.append(pair[::-1])
        else:
            # If we have an incomplete pair (odd string end), just append the single char
            result.append(pair[0])
    
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files
    
    samples = [
        "abcdef",      # Expected: 'bacdef' -> actually 'bacaef'? Let's trace manually.
                      # a,b,c,d,e,f -> b,a,d,c,f,e? No, pairs are (a,b)->ba, (c,d)->dc, (e,f)->fe
                      # So "abcdef" becomes "badcf e"? Wait: 
                      # Pair 1: ab -> ba
                      # Pair 2: cd -> dc  
                      # Pair 3: ef -> fe
                      # Result: bad c f e? No. It should be 'ba' + 'dc' + 'fe' = 'badcfe'.
        "abc",         # Expected: 'bac'? (ab->ba, c stays)
        "",            # Edge case empty string
        "a",           # Single character remains unchanged
        "1234567890"  # Even length digits
    ]

    for sample in samples:
        swapped = swap_adjacent_pairs_optimized(sample)
        print(f'Input: "{sample}" -> Output: "{swapped}"')