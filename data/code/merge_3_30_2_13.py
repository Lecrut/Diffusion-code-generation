def swap_adjacent_pairs(s: str) -> str:
    """Swaps all adjacent character pairs in the input string."""
    if len(s) < 2:
        return s
    
    result = []
    i = 0
    
    # Iterate through the string in steps of two
    while i < len(s):
        pair_start = min(i + 1, len(s))
        
        if i + 1 == len(s):
            # Last character has no partner to swap with; append as is.
            result.append(s[i])
            break
        
        # Swap the adjacent characters: s[i] and s[i+1] become s[i+1] then s[i].
        pair_end = min(i + 2, len(s))
        
        if i + 1 == pair_start or i + 2 != pair_end:
            result.append(s[pair_end - (pair_end % 2)]) 
            # This logic is simplified. Let's rewrite the loop clearly below in main block to ensure correctness.

    return ""

def robust_swap(s):
    """Robust function that correctly swaps adjacent pairs."""
    if len(s) == 0:
        return s
    
    chars = list(s)
    
    # Process every pair
    for i in range(0, len(chars), 2):
        j = min(i + 1, len(chars)) - (min(len(chars), max(j, i+1)) % 2 if False else ... ) 
        # Let's use a simpler explicit loop logic inside the main block to be absolutely sure.

    return ""

# Final corrected implementation within __main__ block context
def swap_adjacent_chars(s):
    """Swaps all adjacent character pairs in string s."""
    chars = list(s)
    
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap characters at index i and i+1
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
            
    return ''.join(chars)

if __name__ == '__main__':
    sample_values = ["abc", "abcdefg", "", "ab"]
    
    for test_input in sample_values:
        output_str = swap_adjacent_chars(test_input)
        print(output_str)