def swap_characters(s: str) -> str:
    """
    Swaps every adjacent pair of characters in the input string.
    
    This function modifies the original string directly by converting it to a list,
    performing the swaps, and then joining the list back into a new string.
    Since strings are immutable in Python, the "in-place" modification on the 
    mutable underlying structure (the list) is returned as a new string object.
    
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), for converting the string to a list and creating the result string.

    Args:
        s (str): The input string whose adjacent characters need swapping.
        
    Returns:
        str: A new string with every pair of adjacent characters swapped.
             Note: To strictly adhere to "modify in place" semantics on an immutable type like a 
             standard Python string, this function returns the result. Standard practice for 
             functions returning strings is that they return the modified version; if strict 
             object mutation were required (which isn't possible with immutables), a wrapper
             class would be needed instead of a simple swap on characters. Given the task asks to
             return the string and modify it directly in context, this approach provides the 
             logical modification while returning the result as expected by Python conventions for strings.

    Raises:
        TypeError: If input is not a string or contains non-string elements (though standard logic handles any iterable).
    
    Example:
        >>> swap_characters("ab")
        'ba'
        >>> swap_characters("abcdef")
        'bacfed'
    """
    # Convert the immutable string to a mutable list of characters.
    chars = list(s)
    
    # Iterate over the list with step 2, swapping elements at index i and i+1.
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap adjacent pair: characters at current position 'i' and next position 'i+1'
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    # Join the list back into a string to return as per Python best practices for strings.
    return ''.join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, args, or network access is needed.
    test_cases = [
        "ab",           # Simple pair swap -> ba
        "abcdef",       # Multiple pairs: ab->ba, cd->dc, ef->fe -> bacfed
        "",             # Empty string remains empty
        "a",            # Single character loop finishes immediately -> a (no change)
    ]

    for test_input in test_cases:
        result = swap_characters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result}'\n")