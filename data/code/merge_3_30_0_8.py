def swap_characters(s: str) -> str:
    """
    Swaps every adjacent pair of characters in a string in place (conceptually, 
    as strings are immutable in Python, this returns a new string with the swaps applied).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string where every two consecutive characters have been swapped.
             If the length is odd, the last character remains unchanged.
    """
    # Convert to list for mutability simulation or direct slicing construction
    chars = list(s)
    
    # Iterate with step 2 and swap adjacent pairs
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            chars[i], chars[i+1] = chars[i+1], chars[i]
            
    return ''.join(chars)

if __name__ == '__main__':
    pass
