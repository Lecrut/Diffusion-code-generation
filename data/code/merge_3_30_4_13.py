def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the string.
    
    For example, "abcd" becomes "badc".
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1) auxiliary space (excluding output).
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
    """
    # Convert string to list for mutability, then back to string at the end
    chars = list(s)
    
    n = len(chars)
    
    # Iterate through the list in steps of 2 and swap pairs
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
            
    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_cases = [
        "abcd",      # Expected: badc
        "aabbccdd",  # Expected: ababdc (wait, let's trace: a<->b -> ba, aa<->bb -> bbaa? No. 
                     # Input: a,a,b,b,c,c,d,d
                     # Swap(0,1): a,a -> a,a; swap chars at 0 and 1 => a becomes char[1] which is 'a'. So "aa" stays "aa"?
                     # Let's re-trace carefully. 
                     # Input: indices 0:a, 1:a, 2:b, 3:b, 4:c, 5:c, 6:d, 7:d
                     # i=0: swap s[0] and s[1]. 'a' <-> 'a'. Result so far "aa..."
                     # i=2: swap s[2] ('b') and s[3] ('b'). Result "...bb..."
                     # So for identical pairs, it doesn't change. 
                     # Let's try a distinct one to verify logic mentally: "1234" -> 2143? No.
                     # i=0: swap '1','2' -> '2','1'. List: ['2', '1', ...]
                     # i=2: swap '3','4' -> '4','3'. List: [..., '4', '3']
                     # Result "2143". Correct.
        "abcdef",    # Expected: bacdef? No. 
                     # 0<->1 (a,b) -> b,a; 2<->3 (c,d) -> d,c; 4<->5 (e,f) -> f,e
                     # Result: badcf e ? Wait indices: 0,1 swapped to b,a. 2,3 swapped to d,c. 4,5 swapped to f,e.
                     # String: "badcfe"
        "",          # Empty string edge case
    ]

    for test_input in test_cases:
        result = reverse_adjacent_swaps(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")