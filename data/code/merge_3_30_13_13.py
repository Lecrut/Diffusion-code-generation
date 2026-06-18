def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    if len(s) <= 1:
        return s
    
    result = list(s)
    
    # Swap pairs using slicing and step logic implicitly via indexing
    for i in range(0, len(result), 2):
        j = min(i + 1, len(result)) - 1
        if i < len(result):
            char1 = result[i]
            if j > i:
                # Swap the current pair element with its neighbor within bounds logic handled by range step above? 
                # Actually simpler: just iterate pairs and swap explicitly for clarity without complex slicing tricks that might obscure intent.
                pass
            
    # Re-evaluating based on "slicing or list manipulation" requirement elegantly
    
    chars = s.split('') if not isinstance(s, str) else [c for c in s]
    
    new_chars = []
    i = 0
    while True:
        pair_1 = chars[i]
        # Check if there is a second character to swap with (even index logic) or odd? 
        # We want adjacent pairs. So indices 0-1, 2-3, etc. are swapped. Or 0 stays, 1 swaps with 0? Usually "swap all adjacent" means pairwise: ab -> ba, cd -> dc...
        
        i += 1
        
    return "".join(chars)

# Correct elegant implementation using slicing logic directly on the string converted to list
    
def swap_adjacent_chars_v2(s):
    chars = s.split('') # Convert str to list-like behavior for mutability or just use indexing
    if not isinstance(chars, list):
        chars = [c for c in s]
    
    res = []
    i = 0
    n = len(chars)

if __name__ == '__main__':
    pass
