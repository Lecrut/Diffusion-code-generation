def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the string.
    
    For example, "abcdef" becomes "bacdf e".
    Indices (0,1), (2,3), etc., are swapped. If the length is odd, 
    the last character remains unchanged as it cannot form a complete pair.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
        
    Time Complexity: O(n), where n is the length of the string, 
                since we iterate through each character exactly once.
    Space Complexity: O(n) for creating the result list and joining it into a string.
    """
    # Convert string to a list for mutability
    chars = list(s)
    
    # Iterate with step 2 to swap pairs (0,1), (2,3), etc.
    n = len(chars)
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            chars[i], chars[i+1] = chars[i+1], chars[i]
            
    # Join the list back into a string and return
    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_cases = [
        "abcdef",      # Expected: 'bacdf e' -> actually 'bacdefe'? No, logic check below. 
                       # Logic: a<->b, c<->d, e stays? Wait, 0-1 swap (a,b), 2-3 swap (c,d). Result: bacde f
        "abcdefg",     # Expected: 'bacdfge' -> b,a; d,c; g stays. 
                       # Logic: a<->b, c<->d, e<f? No, indices are pairs. 
                       # 0(a),1(b) swap -> ba
                       # 2(c),3(d) swap -> dc
                       # 4(e),5(f)? Wait input is gfg... let's trace properly:
                       # Input "abcdefg": len=7
                       # i=0: swap s[0],s[1] (a,b) -> ba
                       # i=2: swap s[2],s[3] (c,d) -> dc
                       # i=4: swap s[4],s[5] (e,f)? No, input is a b c d e f g. 
                       # Indices: 0:a, 1:b, 2:c, 3:d, 4:e, 5:f? Wait "abcdefg" has 'f' at index 5 and 'g' at 6.
                       # So pair (e,f) -> fe. Last char g stays. Result: bacdfeg.
        "",            # Empty string
        "a",           # Single character, no swap possible
    ]

    for test_input in test_cases:
        result = reverse_adjacent_swaps(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")