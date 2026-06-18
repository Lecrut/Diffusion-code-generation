def swap_characters(s: str) -> str:
    """
    Swaps every adjacent pair of characters in the input string in place 
    (by converting to a list, swapping elements, and joining back into a string).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with swapped adjacent pairs. Note that since strings are immutable,
             the function effectively returns a modified version of the original structure 
             but does not mutate the original Python object in place as strictly required by immutability rules;
             however, to adhere to "modify directly" while respecting language constraints:
             We convert to list (mutable), swap elements from start to end with step 2, join back.
             
    Note on 'in-place': Strings are immutable in Python. True in-place modification is impossible 
    without side effects on external references or converting the whole thing into a mutable structure temporarily.
    This implementation converts the string to a list of characters for mutation (which represents logical in-place change),
    performs the swaps, and returns the resulting joined string.
    
    >>> swap_characters("ab")
    'ba'
    >>> swap_characters("abcd")
    'badc'
    >>> swap_characters("")
    ''
    """
    # Convert to list of characters for mutability (required step before true modification)
    chars = list(s)
    
    # Iterate over the string with a stride of 2, up to half its length
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap characters at index i and i+1
            chars[i], chars[i+1] = chars[i+1], chars[i]
    
    return ''.join(chars)

if __name__ == '__main__':
    test_cases = [
        "ab",
        "abcd",
        "",
        "hello world!",
        "a"  # Odd length string, last char stays put
    ]

    for text in test_cases:
        result = swap_characters(text)
        print(f'Input: "{text}" -> Output: "{result}"')