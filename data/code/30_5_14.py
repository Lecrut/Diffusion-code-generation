import string

def swap_even_odd_indices(s: str) -> str:
    """
    Swaps characters at even indices with those at odd indices in a string.
    
    For example, if input is "abcd", output becomes "badc".
    If the length of the string is odd (e.g., "abc"), only pairs are swapped 
    up to the last complete pair, leaving the final character unchanged.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with even and odd indexed characters swapped.
    """
    result = []
    length = len(s)
    
    # Iterate through pairs of indices (i, i+1) where i is even
    for i in range(0, length - 1, 2):
        if i + 1 < length:
            # Swap characters at index i and i+1
            result.append(s[i + 1])
            result.append(s[i])
    
    return ''.join(result)

if __name__ == '__main__':
    pass
