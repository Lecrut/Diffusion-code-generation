def swap_characters(s: str) -> str:
    """
    Swaps adjacent pairs of characters in the input string.
    
    For a string 'abcde', it becomes 'bacd e' (assuming spaces are handled as chars too).
    The last character if odd remains unchanged because there is no pair for it.
    
    Args:
        s (str): Input string to modify and return.
        
    Returns:
        str: The modified string with adjacent characters swapped in place logic applied 
             via concatenation since strings are immutable, but the function name implies 
             'in-place' conceptually by returning a fully transformed version of its input.
    
    Note: Python strings are immutable. True "in-place" modification is not possible without 
    converting to a list first and then joining back into a string. The return value reflects 
    the state after swapping.
    """
    # Convert string to list for mutability (simulating in-place swap)
    char_list = list(s)
    
    # Iterate over the list with step 2, processing pairs [i, i+1]
    for i in range(0, len(char_list), 2):
        if i + 1 < len(char_list):
            # Swap current character at index i with next character at index i+1
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
    
    # Convert list back to string and return (effectively returning the modified version)
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values that run without user input or external dependencies
    test_cases = [
        "hello",      # Expected: 'ehll o' -> actually swapping h-e, l-l, e-o => ehlo? 
                      # Wait, let's trace carefully.
                      # Input: h, e, l, l, o (indices 0,1,2,3,4)
                      # Swap(0,1): e, h
                      # Swap(2,3): l, l -> still l,l
                      # Index 4 is left alone.
                      # Result: ehlll? No. 
                      # Let's re-trace "hello":
                      # i=0: swap char_list[0]('h') and [1]('e') -> ['e', 'h', ...]
                      # i=2: swap char_list[2]('l') and [3]('l') -> no change.
                      # i=4: loop ends because 5 is not < 5? Range(0, 5, 2) gives 0, 2. 
                      # So index 4 ('o') remains at end.
                      # Result string should be "ehllo". Wait previous thought was wrong on logic trace.
                      # Correct Trace for "hello":
                      # List: ['h', 'e', 'l', 'l', 'o']
                      # i=0: swap h,e -> e,h,l,l,o
                      # i=2: swap l,l (index 2 and 3) -> still l,l. Result: e,h,l,l,o.
                      # Wait, index 4 is skipped in loop? Range(0,5,2) yields 0, 2. 
                      # Yes, so 'o' stays at end. Correct result: "ehllo". My manual trace earlier was confused about indices.
        "abcdef",      # Expected: ba cd ef -> b a c d e f ? No.
                      # List: [a,b,c,d,e,f]
                      # i=0: swap a,b -> b,a...
                      # i=2: swap c,d -> ...d,c? 
                      # Wait, index 2 is 'c', index 3 is 'd'. Swap them -> d,c.
                      # Result: b a d c e f.
        "xyz",         # Odd length. x,y,z. y stays middle relative to pair logic? No.
                      # i=0: swap x,y -> y,x.z
                      # Loop ends at 2 (not <3). z remains.
                      # Result: yxz.
    ]

    for original in test_cases:
        result = swap_characters(original)
        print(f"Input: '{original}'")
        print(f"Output: '{result}'\n")