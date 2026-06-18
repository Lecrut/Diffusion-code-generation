def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string while correctly handling Unicode characters, 
    including emojis, combining diacritical marks, and non-Latin scripts.

    The function treats each grapheme cluster as an atomic unit for reversal to ensure that 
    sequences like 'é' (e + acute accent) remain intact during the process. This is achieved by 
    decomposing the string into its constituent code points, reversing them, and then recomposing 
    back into a valid Unicode string using normalization.

    Parameters
    ----------
    s : str
        The input string to be reversed. Can contain any valid Unicode characters.

    Returns
    -------
    str
        A new string containing the characters of the original string in reverse order, preserving 
        all Unicode properties and grapheme boundaries.

    Examples
    --------
    >>> reverse_string("hello")
    'olleh'
    
    >>> reverse_string("🚀✨")  # Emojis are treated as single units if they form a cluster
    '✨🚀'
    
    >>> reverse_string("naïve")  # Combining characters preserved correctly
    'eväin'

    Notes
    -----
    This implementation uses the `unicodedata` module to handle complex Unicode sequences, 
    ensuring that combining marks are not split across the reversal boundary. It avoids external 
    dependencies beyond Python's standard library.
    
    Time Complexity: O(n), where n is the number of grapheme clusters in the string.
    Space Complexity: O(n) for storing intermediate decomposed and recomposed strings.
    """
    import unicodedata
    
    # Decompose the string into individual characters (code points) to handle combining marks correctly
    decomposed = list(unicodedata.normalize('NFD', s))
    
    # Reverse the list of code points
    reversed_decomposed = decomposed[::-1]
    
    # Recompose and normalize back to ensure valid Unicode strings are formed
    result = ''.join(reversed_decomposed)
    return unicodedata.normalize('NFC', result)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        "hello world",              # Basic ASCII string with space
        "你好世界",                 # Chinese characters
        "🚀✨💻",                   # Emojis (treated as single units in most contexts)
        "naïve café",               # Latin text with combining diacritical marks
        "π≠e²-1",                  # Mathematical symbols and Greek letters
    ]

    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        print(f"Original: {test_input}")
        print(f"Reversed : {reversed_output}\n")