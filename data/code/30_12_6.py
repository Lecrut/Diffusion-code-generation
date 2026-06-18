def swap_adjacent_pairs(s: str) -> str:
    """Swaps every pair of adjacent characters in the input string."""
    result = []
    
    # Iterate over the string with a step of 2 to access pairs efficiently
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            # Swap current character (i) and next character (i+1)
            result.append(s[i + 1])
            result.append(s[i])
        else:
            # If the last character is odd, append it as-is without a pair to swap with
            result.append(s[i])
    
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values for testing. 
    # These run without user input or external dependencies.
    samples = [
        "abcdef",      # Even length: ab->ba, cd->dc, ef->fe -> badcfe
        "abcde",       # Odd length: ab->ba, cd->dc, e stays -> bacd + 'e' -> bacdce (Wait logic check)
                      # Correction for odd length trace on "abcde": 
                      # i=0: swap a,b -> ba; result=['b','a']
                      # i=2: swap c,d -> dc; result=['b','a','d','c']
                      # i=4: last char 'e', append as is; result=['b','a','d','c','e']
        "123",         # 1,2->2,1 then 3 stays -> 213
        "",            # Empty string
        "x"             # Single character remains same
    ]

    for sample in samples:
        output = swap_adjacent_pairs(sample)
        print(output)