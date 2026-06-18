def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the string.
    
    For example, if n is even, it swaps s[0] with s[1], s[2] with s[3], etc.
    If n is odd, the last character remains unchanged as there is no partner for it.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped in pairs.
    """
    # Convert string to list of characters since strings are immutable in Python
    chars = list(s)
    n = len(chars)
    
    # Iterate through the list with a step of 2, swapping elements at i and i+1
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    # Join the list back into a string and return it
    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_cases = [
        "abcdef",      # Even length: ab -> ba, cd -> dc, ef -> fe => bacdf e (wait, swap pairs: a<->b, c<->d, e<->f)
                      # Expected: badcfe
        "abcde",       # Odd length: last char stays. a<->b, c<->d, e remains => bacde
        "",            # Empty string
        "a",           # Single character
        "1234567890"  # Digits example
    ]

    for test_input in test_cases:
        result = reverse_adjacent_swaps(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")