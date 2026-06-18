def swap_even_odd_indices(s: str) -> str:
    """
    Swaps characters at even indices with their neighbors (odd indices).
    
    For a string of length n (0-indexed):
    - Index 0 swaps with index 1, index 2 with index 3, etc.
    - If the last character is at an odd position and unmatched, it remains in place 
      as there is no even neighbor to swap with on its right side? No:
      
      Actually, let's re-read carefully: "swaps every character with its neighbor"
      This implies pairing (0,1), (2,3), etc.
      
      If length is odd:
        - Pairs are formed for indices where both exist in the pair.
        - The last element at an even index has no odd-indexed right neighbor? 
          Or does it mean swapping left-right regardless of parity?
        
      Let's interpret "swaps characters at even indices with ... odd indices" as:
      s[i] <-> s[j] where i is even and j = i+1.
      
      Example: "abcde" (len 5) -> pairs (0,1), (2,3). Index 4 ('e') has no pair? 
      But the prompt says "handle strings of odd length correctly". 
      Usually this means if there's a leftover at the end with even index, it stays alone.
      
    Args:
        s (str): Input string
        
    Returns:
        str: String with swapped adjacent characters starting from index 0 and step 2.
    """
    chars = list(s)
    
    # Iterate through indices in steps of 2 to form pairs (i, i+1)
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap characters at index i and i+1
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return ''.join(chars)

if __name__ == '__main__':
    pass
