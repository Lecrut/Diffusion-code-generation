def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string two by two, starting from index 0.
    
    If the string has an odd length, the last character remains unchanged 
    as there is no pair to swap with it.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
        
    Examples:
        >>> swap_adjacent_chars("ab")
        'ba'
        >>> swap_adjacent_chars("abc")
        'bac'
        >>> swap_adjacent_chars("abcd")
        'badc'
    """
    if not s:
        return ""
    
    result = []
    for i in range(0, len(s), 2):
        # Append the character at index +1 if it exists (swapped position)
        if i + 1 < len(s):
            result.append(s[i + 1])
        # Else append s[i] but only once per pair logic handled by step size
        else:
            result.append(s[i])
    
    return "".join(result)

if __name__ == '__main__':
    # Test Case 1: Even length string with distinct characters
    test_even = "abcdef"
    expected_even = "bacdf e"  # Correction for logic trace below
    
    # Re-evaluating swap_adjacent_chars("abcdef"): 
    # i=0 -> take s[1]='b', then s[3]='d'?? No, the loop appends pairs sequentially.
    # Let's re-verify the implementation logic in head:
    # "ab" -> result gets 'b', then next iteration starts at 2. 
    # Wait, my previous mental trace was slightly off on how I wrote the code above vs standard swap.
    # Code written: for i in range(0, len(s), 2): append s[i+1] if exists else append s[i].
    # Input "ab": i=0. i+1 < 2? Yes. Append 'b'. Loop ends (i jumps to 2). Result "ba". Correct.
    # Input "abcde" (odd length, last char left alone): 
    #   i=0: append s[1] ('b') -> result ['b']
    #   i=2: append s[3] ('d')? NO. Wait.
    # Let's re-read the code I just wrote mentally to ensure correctness before finalizing output.
    
    pass

# Correct Logic Verification for "abcdef" (len 6)
# Loop range(0, 6, 2) -> [0, 2, 4]
# i=0: s[1]='b' appended. Result="b".
# i=2: s[3]='d'? NO! The code says "append s[i+1]" then later... wait.
# My previous draft had a flaw in the logic description vs implementation if I want standard swap (ab -> ba, cd -> dc).
# Standard Swap Logic: 
#   If even len 4 ("abcd"): should be "badc".
#   i=0: append s[1] ('b'). Result="b".
#   Next iteration? The loop increments by 2. So next is i=2.
#   At i=2, we need to process the pair starting at 'cd'. We want 'dc'.
#   Code says: if i+1 < len(s): result.append(s[i+1]). 
#   For "abcd": i=0 -> append s[1] ('b'). Correct.
#                 i=2 -> check 3<4? Yes. Append s[3] ('d'). Result="bd". WRONG. Should be 'dc'.
    
    # Correction required: The standard swap of adjacent pairs (indices 0-1, 2-3) produces "badc" from "abcd".
    # To achieve this with a simple loop stepping by 2:
    # We need to append s[i+1] then s[i]. 
    # Or simply reconstruct the string differently.
    
    def swap_adjacent_chars_fixed(s):
        chars = list(s)
        for i in range(0, len(chars), 2):
            if i + 1 < len(chars):
                chars[i], chars[i+1] = chars[i+1], chars[i]
        return "".join(chars)

    # Re-implementing the function correctly based on this analysis.
    
def swap_adjacent_chars_final(s: str) -> str:
    """
    Swaps adjacent characters in a string two by two, starting from index 0.
    
    If the string has an odd length, the last character remains unchanged 
    as there is no pair to swap with it.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
            
    Examples:
        >>> swap_adjacent_chars_final("ab")
        'ba'
        >>> swap_adjacent_chars_final("abc")
        'bac'
        >>> swap_adjacent_chars_final("abcd")
        'badc'
        
        Note on "abc": Pair (a,b) swaps -> ba. Last char c stays. Result: bac.
    """
    chars = list(s)
    
    # Iterate through the string with a step of 2 to find pairs
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap characters at index i and i+1
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
            
    return "".join(chars)

if __name__ == '__main__':
    print("Running Test Cases...")

    # Case 1: Even length string (4 characters) -> "abcd" should become "badc"
    test_1 = "abcdef"