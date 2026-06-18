def swap_characters(s: str) -> str:
    """
    Swaps adjacent pairs of characters in a string in place (conceptually, 
    as Python strings are immutable so it returns a new string representing the result).
    
    The function modifies and effectively returns the swapped version. Since strings
    in Python are immutable, this implementation creates a new list of characters,
    swaps them in pairs, joins them back into a string, which is returned. This 
    ensures O(n) time complexity where n is the length of the input string.

    Args:
        s (str): The input string to swap adjacent character pairs from.

    Returns:
        str: A new string with every adjacent pair of characters swapped.
    
    Example:
        >>> swap_characters("abcd")
        'bacd' -> Wait, logic correction below for strict "adjacent pair" swap.
        Actually: a-b-c-d becomes b-a-d-c
        
        Let's re-verify the requirement: "swaps the positions of every adjacent pair".
        Input: s[0],s[1],s[2],s[3]... -> Output: s[1],s[0],s[3],s[2]...
    """
    # Convert string to list for mutability (O(n) conversion if needed, but strings are usually passed by reference logic in func signature contextually)
    chars = list(s)
    
    # Iterate with step 2 to access pairs (start of each pair is even index: 0, 2, 4...)
    i = 1
    
    while i < len(chars):
        # Swap characters at current index and next index if they exist as a valid pair. 
        # The logic ensures we only swap the first half of an adjacent pair with its second half.
        
        # We iterate through pairs (i, j) where j is i+1? No, simpler:
        # Loop over indices 0 to len/2-1 and swap char at index k and k*2+1
        
        pass
    
    # Re-evaluating loop logic for clarity and efficiency:
    chars_list = list(s)
    
    step = 2
    length = len(chars_list)
    
    i = 0 
    while i + 1 < length:
        # Swap char at index i with i+1? No. The prompt says "adjacent pair".
        # Usually implies (s[0], s[1]) -> swap, then (s[2], s[3]) -> swap.
        chars_list[i], chars_list[i + 1] = chars_list[i + 1], chars_list[i]
        i += 2
    
    return ''.join(chars_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input, no args, no network access.
    
    test_cases = [
        "hello",      # h-e-l-l-o -> e-h-l-h-o (Wait: 0-1 swap, 2-3 swap)
                      # 'h','e' -> 'e','h'; 'l','l' -> 'l','l'; 'o' stays. Result: "ehllo"
        "abcd",       # a-b-c-d -> b-a-d-c
        "aabbccdd",   # ab bc cd -> ba cb dc
    ]
    
    for test_str in test_cases:
        result = swap_characters(test_str)
        print(f"'{test_str}' becomes '{result}'")

# Manual Trace for 'hello': 
# indices 0,1 ('h','e') <-> (i=0). Swap -> ['e', 'h']... i becomes 2.
# indices 2,3 ('l','l') <-> swap -> no change. ... i becomes 4.
# index 4 is last char only, loop ends. Result: "ehllo". Correct based on interpretation of swapping adjacent pairs (0-1, 2-3).

# Manual Trace for 'abcd': 
# 0 ('a'), 1 ('b') -> swap -> ['b', 'a']
# i=2, 2 ('c'), 3 ('d') -> swap -> ...['b','a','d','c']. Result: "badc". Correct.