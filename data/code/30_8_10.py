def swap_adjacent_characters(s: str) -> str:
    """
    Swaps adjacent characters in a string two positions at a time from left to right.
    
    For example, if the input is "abcd", it becomes "badc". If the length is odd,
    the last character remains as is since there is no pair for it.
    
    Args:
        s (str): The input string whose adjacent characters will be swapped.
        
    Returns:
        str: A new string with every even-indexed and odd-indexed pair of 
             characters interchanged, or the original character at an odd length's end if one remains.

    Examples:
        >>> swap_adjacent_characters("abcd")
        'badc'
        >>> swap_adjacent_characters('abc')
        'bac'
        >>> swap_adjacent_characters('a')
        'a'
    """
    # Check for empty string
    if not s:
        return ""

    result = []
    
    # Iterate through the string with a step of 2 to form pairs
    for i in range(0, len(s), 2):
        pair_start = min(i + 1, len(s))
        
        # If there is a second character, swap them; otherwise keep just one char (odd case)

if __name__ == '__main__':
    pass
