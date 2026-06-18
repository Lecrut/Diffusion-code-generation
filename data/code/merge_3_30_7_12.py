def swap_adjacent_chars(char_list):
    """
    Iterates through a list of characters, swapping each character at index i 
    with the character at index i+1 for all valid indices where both exist.
    
    Args:
        char_list (list): A mutable list containing single-character strings or other elements.
        
    Returns:
        None: Modifies the input list in place.

    Example Usage:
        >>> chars = ['a', 'b', 'c']
        >>> swap_adjacent_chars(chars)
        >>> print(''.join(chars))
        ab -> ba, bc -> cb => b a c becomes a b c swapped sequentially? 
        Wait, the logic is i swaps with i+1. 
        For [0], swap 0 and 1: ['a','b'] -> ['b','a']. Then for index 1 (now 'c'), no next element if length was originally 3?
        Actually, let's trace carefully based on "for all valid i". Usually this means iterating through the list 
        and performing swaps. The order of operations matters in a single pass vs multiple passes.
        
        Re-reading: "swaps the character at index $i$ with the character at index $i+1$ for all valid $i$."
        This phrasing is slightly ambiguous regarding iteration order (sequential left-to-right updating). 
        However, typically such problems imply a single pass where you swap adjacent pairs as you encounter them.
        
        Let's assume standard sequential traversal: i=0 swaps 0&1, then move to next position? Or does it mean 
        perform all possible swaps simultaneously based on original indices? 
        Given "iterates through", I will implement a single pass loop where at each step `i`, we swap `list[i]` and `list[i+1]`.
        
        Trace [a, b, c]:
        i=0: Swap 0 & 1. List becomes [b, a, c]. Next i should be... 
        If I increment i to 1 now: Check index 1 ('a') with index 2 ('c'). Swap -> [b, c, a].
        
        Alternative interpretation (simultaneous): Original pairs are (0,1), (1,2). Swaps happen based on original state? 
        But "iterates through" suggests sequential execution. I will go with the sequential update approach as it's standard for in-place iteration tasks unless specified otherwise.
    """
    
    # Ensure we have a mutable list of characters/strings
    if not isinstance(char_list, list):
        raise TypeError("Input must be a mutable list.")

    n = len(char_list)
    i = 0
    
    while i < n - 1:
        current_char = char_list[i]
        next_char = char_list[i + 1]
        
        # Perform the swap in place (since it's already a list, we just exchange values)
        char_list[i], char_list[i+1] = char_list[i+1], char_list[i]
        
        i += 1

    return None

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input/args/network/files)
    
    # Sample string converted to a list of characters for mutability efficiency
    original_string = "abcdef"
    char_list = [c for c in original_string]

    print(f"Original: {''.join(char_list)}")
    
    swap_adjacent_chars(char_list)
    
    result_string = ''.join(char_list)
    print(f"After swapping adjacent characters sequentially:")
    print(result_string)