def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string.
    
    For example, "abcdef" becomes "bacdf e".
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) if ignoring output storage (output size proportional to input).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with every pair of characters swapped.
    """
    # Convert string to a list for mutability, then back to string at the end
    chars = list(s)
    
    length = len(chars)
    i = 0
    
    while i < length - 1:
        # Swap current character with next one if pair exists within bounds of loop logic below handled by step size
        # We only swap pairs (i, i+1), so we increment by 2 to skip already processed positions in this iteration's context 
        # but actually here we are iterating the whole string. The while condition ensures safety for odd lengths.
        
        if length > i + 1:
            chars[i], chars[i+1] = chars[i+1], chars[i]
        i += 2
        
    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the block runs without user input or file access.
    
    test_cases = [
        "abcdef",      # Expected: "bacdf e" -> actually "ba cd fe" wait logic check: a<->b, c<->d, e stays? No pairs only if even length? 
                      # Logic trace: i=0 swap 0/1 (a,b). i becomes 2. char at 2 is 'c', swap with 3 ('d'). i becomes 4. char at 4 is 'e'. len-1 = 5. Condition true. Swap e/f? No f doesn't exist. 
                      # Wait, my loop logic in thought process was slightly off regarding odd length ending characters.
                      # Let's re-evaluate the swap rule: "swap index 0 with 1, 2 with 3...". Unpaired last char remains alone if string is odd? Yes.
        "abcdef",      # Expected result: "bac dfe" -> "ba cdf e"? No. 
                      # Input: a b c d e f
                      # Swap (0,1): b a ...
                      # Swap (2,3): . . d c e f -> bacdcf? Wait indices 4 and 5 are 'e','f'. Swap them -> ba cd fe. Correct result "bacdfe" is wrong if I swap e,f manually in head... 
                      # Let's trace carefully:
                      # Original: a b c d e f (len=6)
                      # i=0: swap s[0],s[1] -> b, a ... rest unchanged. List: [b, a, c, d, e, f]
                      # i+=2 => i=2. Swap s[2],s[3]. Original list now has 'c','d' at 2,3. They swap to 'd','c'. 
                      # List: [b, a, d, c, e, f]
                      # i+=2 => i=4. Swap s[4],s[5]. 'e','f' -> 'f','e'.
                      # Final: "badcf ef" ?? No. b,a,d,c,f,e -> "bacdfe". 
                      
    ]

    results = []
    
    for input_str in test_cases:
        res = reverse_adjacent_swaps(input_str)
        results.append(f'Input: "{input_str}" => Output: "{res}"')
        
    print("\n".join(results))