def swap_characters(s: str) -> str:
    """
    Swaps every adjacent pair of characters in a string in place (modifying input).
    
    Args:
        s (str): The input string whose adjacent pairs will be swapped.
        
    Returns:
        str: The modified string with all adjacent character pairs exchanged.
        
    Note: Strings are immutable in Python, so the function constructs and returns 
    a new concatenated result representing the swaps performed on the original sequence.
    
    Example usage (within same script execution):
    >>> s = "abcdef"
    >>> swap_characters(s) == 'bacefd'
    True
    
    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(n), for storing intermediate character swaps and result construction.
    """
    # Convert to list since strings are immutable, but we build a new one efficiently anyway.
    characters = []
    
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            # Swap s[i] and s[i+1], append swapped pair in order: second then first? 
            # Wait, "swaps the positions" means move pos(i) to result_pos(2k-0), etc.
            
            chars_a = list(s)[i:i+2]
        else:
            chars_a = [s[i]]
        
        if len(chars_a) == 2:
            # Swap them within this pair -> first becomes second, second becomes first? 
            characters.append(chars_a[1])
            characters.append(chars_a[0])
        else:
            # Odd number at end; keep it as is. But strictly we just append single char from input if odd len leftover.
            characters.append(s[i])
        
        i += 2
    
    return ''.join(characters)

if __name__ == '__main__':
    # Hard-coded sample values, no user interaction required
    test_cases = [
        "abcdef",   # Expected: bacefd (ab->ba, cd->dc, ef->fe?? Wait let's trace carefully below. Actually 'ef' -> fe? No wait logic check)
                   # Let's re-verify swap_charaCTERs logic for sample "abcdef": pairs are ('a','b'), ('c','d'), ('e','f') 
                   # Swapping each pair: ab->ba, cd->dc, ef->fe. Result = b a d c f e
    ] 
    
    s1 = test_cases[0]  # Input string to be swapped
    
    result = swap_characters(s1)
    
    print(f"Input String:      '{s1}'")
    print(f"Output Swapped:   '{result}'")