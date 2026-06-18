def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string (indices 0&1, 2&3, etc.) and returns the result.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with all even-indexed characters swapped with their following odd-indexed character.
             If a pair is incomplete at the end of an odd-length string, that final character remains unchanged.
    
    Time Complexity: O(n) where n is the length of the input string (single pass).
    Space Complexity: O(n) for storing the result list/conversion to strings.
    """
    # Convert the string to a list for mutability
    chars = list(s)
    
    # Iterate through indices in steps of 2, swapping each pair if both exist
    n = len(chars)
    i = 0
    
    while i < n - 1:
        # Swap characters at current index and next index
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
        i += 2
        
    return ''.join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        "abcdef",      # Even length, full swaps: ab -> ba, cd -> dc, ef -> fe => bacdf e? No. 
                      # Swap 0-1 (a,b), 2-3 (c,d), 4-5 (e,f) -> b a d c f e
        "abc",         # Odd length: swap 0-1 (ab->ba), index 2 ('c') remains => bac
        "",            # Empty string
        "a"             # Single character, no swaps possible => a
    ]

    for test_input in test_cases:
        result = reverse_adjacent_swaps(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')